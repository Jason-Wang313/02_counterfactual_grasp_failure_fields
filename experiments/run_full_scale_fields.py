from __future__ import annotations

import argparse
import csv
import json
import math
import random
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results" / "full_scale"
FIGURES = RESULTS / "figures"
PAPER_FIGURES = ROOT / "paper" / "figures"
PAPER_TABLES = ROOT / "paper" / "tables"


BASELINES = [
    "no_repair",
    "scalar_random_sign",
    "scalar_global_sign",
    "scalar_prior_sample",
    "uniform_signed",
    "nearest_contact",
    "noisy_signed_margin",
    "signed_margin",
    "counterfactual_field",
]

FIELDS = [
    "suite",
    "baseline",
    "seed",
    "case_id",
    "contact_count",
    "positive_prior",
    "noise_scale",
    "mask_rate",
    "limit_scale",
    "active_count",
    "error_sign",
    "initial_error",
    "initial_margin",
    "field_feasible",
    "success",
    "post_margin",
    "effort",
    "field_effort",
    "disagreement_l2",
    "correct_direction",
    "clipped",
]


@dataclass(frozen=True)
class LinearContactParams:
    weights: tuple[float, ...]
    costs: tuple[float, ...]
    limits: tuple[float, ...]
    active: tuple[bool, ...]
    radius: float


@dataclass(frozen=True)
class LinearContactState:
    contacts: tuple[float, ...]
    target: float


@dataclass(frozen=True)
class Projection:
    delta: tuple[float, ...]
    feasible: bool
    clipped: bool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--out", type=Path, default=RESULTS)
    parser.add_argument("--summarize-only", action="store_true")
    return parser.parse_args()


def ensure_dirs() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    PAPER_FIGURES.mkdir(parents=True, exist_ok=True)
    PAPER_TABLES.mkdir(parents=True, exist_ok=True)


def dot(a: Iterable[float], b: Iterable[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def error_coordinate(state: LinearContactState, params: LinearContactParams) -> float:
    return state.target - dot(params.weights, state.contacts)


def margin(state: LinearContactState, params: LinearContactParams) -> float:
    return params.radius - abs(error_coordinate(state, params))


def effort(delta: Iterable[float], costs: Iterable[float]) -> float:
    return math.sqrt(sum(c * d * d for c, d in zip(costs, delta)))


def apply_delta(state: LinearContactState, delta: Iterable[float]) -> LinearContactState:
    return LinearContactState(tuple(y + d for y, d in zip(state.contacts, delta)), state.target)


def in_limits(state: LinearContactState, params: LinearContactParams) -> bool:
    return all(abs(y) <= limit + 1e-9 for y, limit in zip(state.contacts, params.limits))


def is_success(state: LinearContactState, params: LinearContactParams) -> bool:
    return in_limits(state, params) and margin(state, params) >= -1e-9


def projection_delta(
    state: LinearContactState,
    params: LinearContactParams,
    required_balance_change: float,
    weights: tuple[float, ...] | None = None,
    use_limits: bool = True,
    active_override: tuple[bool, ...] | None = None,
) -> Projection:
    ws = weights if weights is not None else params.weights
    active = active_override if active_override is not None else params.active
    n = len(ws)
    delta = [0.0] * n
    lower: list[float] = []
    upper: list[float] = []
    for y, limit, is_active in zip(state.contacts, params.limits, active):
        if not is_active:
            lower.append(0.0)
            upper.append(0.0)
        elif use_limits:
            lower.append(-limit - y)
            upper.append(limit - y)
        else:
            lower.append(-1.0e9)
            upper.append(1.0e9)

    free = {i for i in range(n) if active[i] and abs(ws[i]) > 1e-12}
    residual = required_balance_change
    clipped = False
    feasible = True

    while True:
        if abs(residual) <= 1e-10:
            break
        denom = sum((ws[i] * ws[i]) / params.costs[i] for i in free)
        if denom <= 1e-12:
            feasible = False
            break
        proposal = {i: residual * ws[i] / params.costs[i] / denom for i in free}
        violations = []
        for i, d in proposal.items():
            if d < lower[i] - 1e-10:
                violations.append((lower[i] - d, i, lower[i]))
            elif d > upper[i] + 1e-10:
                violations.append((d - upper[i], i, upper[i]))
        if not violations:
            for i, d in proposal.items():
                delta[i] = d
            break
        _, idx, bound = max(violations)
        delta[idx] = bound
        residual -= ws[idx] * bound
        free.remove(idx)
        clipped = True

    achieved = dot(ws, delta)
    if abs(achieved - required_balance_change) > 1e-7:
        feasible = False
    return Projection(tuple(delta), feasible, clipped)


def true_field(state: LinearContactState, params: LinearContactParams, use_limits: bool = True) -> Projection:
    e = error_coordinate(state, params)
    if abs(e) <= params.radius:
        return Projection(tuple(0.0 for _ in params.weights), True, False)
    required = e - math.copysign(params.radius, e)
    return projection_delta(state, params, required, use_limits=use_limits)


def random_params(
    rng: random.Random,
    contact_count: int,
    mask_rate: float = 0.0,
    limit_scale: float = 1.0,
    cost_spread: float = 1.0,
) -> LinearContactParams:
    weights = []
    costs = []
    limits = []
    active = []
    for _ in range(contact_count):
        sign = -1.0 if rng.random() < 0.5 else 1.0
        weights.append(sign * rng.uniform(0.35, 1.65))
        log_cost = rng.uniform(-cost_spread, cost_spread)
        costs.append(math.exp(log_cost))
        limits.append(limit_scale * rng.uniform(0.55, 1.25))
        active.append(rng.random() >= mask_rate)
    if not any(active):
        active[rng.randrange(contact_count)] = True
    radius = rng.uniform(0.06, 0.34)
    return LinearContactParams(tuple(weights), tuple(costs), tuple(limits), tuple(active), radius)


def sample_case(
    rng: random.Random,
    params: LinearContactParams,
    positive_prior: float = 0.5,
    near_limits: bool = False,
    require_field_feasible: bool = True,
) -> LinearContactState:
    for _ in range(500):
        contacts = []
        for limit in params.limits:
            scale = rng.uniform(0.72, 0.98) if near_limits else rng.uniform(0.0, 0.65)
            sign = -1.0 if rng.random() < 0.5 else 1.0
            contacts.append(sign * scale * limit)
        sign_e = 1.0 if rng.random() < positive_prior else -1.0
        excess = rng.uniform(0.025, 0.72)
        target = dot(params.weights, contacts) + sign_e * (params.radius + excess)
        state = LinearContactState(tuple(contacts), target)
        field = true_field(state, params, use_limits=True)
        if not require_field_feasible or field.feasible:
            return state
    return state


def canonical_scalar_delta(
    state: LinearContactState,
    params: LinearContactParams,
    sign_guess: int,
    use_limits: bool = True,
) -> Projection:
    e = error_coordinate(state, params)
    magnitude = max(0.0, abs(e) - params.radius)
    required = float(sign_guess) * magnitude
    return projection_delta(state, params, required, use_limits=use_limits)


def uniform_signed_delta(state: LinearContactState, params: LinearContactParams) -> Projection:
    e = error_coordinate(state, params)
    required = e - math.copysign(params.radius, e)
    active = [i for i, flag in enumerate(params.active) if flag]
    denom = sum(params.weights[i] for i in active)
    if abs(denom) <= 1e-12:
        return Projection(tuple(0.0 for _ in params.weights), False, False)
    d = required / denom
    delta = [0.0 for _ in params.weights]
    clipped = False
    for i in active:
        low = -params.limits[i] - state.contacts[i]
        high = params.limits[i] - state.contacts[i]
        if d < low:
            delta[i] = low
            clipped = True
        elif d > high:
            delta[i] = high
            clipped = True
        else:
            delta[i] = d
    return Projection(tuple(delta), True, clipped)


def nearest_contact_delta(state: LinearContactState, params: LinearContactParams) -> Projection:
    e = error_coordinate(state, params)
    required = e - math.copysign(params.radius, e)
    active = [i for i, flag in enumerate(params.active) if flag and abs(params.weights[i]) > 1e-12]
    if not active:
        return Projection(tuple(0.0 for _ in params.weights), False, False)
    idx = max(active, key=lambda i: abs(params.weights[i]) / math.sqrt(params.costs[i]))
    d = required / params.weights[idx]
    low = -params.limits[idx] - state.contacts[idx]
    high = params.limits[idx] - state.contacts[idx]
    clipped = d < low or d > high
    d = min(high, max(low, d))
    delta = [0.0 for _ in params.weights]
    delta[idx] = d
    return Projection(tuple(delta), not clipped, clipped)


def noisy_signed_delta(state: LinearContactState, params: LinearContactParams, rng: random.Random, noise_scale: float) -> Projection:
    e = error_coordinate(state, params)
    scale = max(params.radius, abs(e), 1e-6)
    e_hat = e + rng.gauss(0.0, noise_scale * scale)
    radius_hat = max(0.01, params.radius * (1.0 + rng.gauss(0.0, 0.5 * noise_scale)))
    weights_hat = tuple(w * (1.0 + rng.gauss(0.0, noise_scale)) for w in params.weights)
    if abs(e_hat) <= radius_hat:
        required = 0.0
    else:
        required = e_hat - math.copysign(radius_hat, e_hat)
    return projection_delta(state, params, required, weights=weights_hat, use_limits=True)


def repair_for_baseline(
    baseline: str,
    state: LinearContactState,
    params: LinearContactParams,
    rng: random.Random,
    positive_prior: float,
    noise_scale: float,
) -> Projection:
    e = error_coordinate(state, params)
    sign_true = 1 if e >= 0.0 else -1
    if baseline == "no_repair":
        return Projection(tuple(0.0 for _ in params.weights), True, False)
    if baseline == "counterfactual_field":
        return true_field(state, params, use_limits=True)
    if baseline == "signed_margin":
        return canonical_scalar_delta(state, params, sign_true, use_limits=True)
    if baseline == "scalar_random_sign":
        return canonical_scalar_delta(state, params, 1 if rng.random() < 0.5 else -1, use_limits=True)
    if baseline == "scalar_global_sign":
        return canonical_scalar_delta(state, params, 1 if positive_prior >= 0.5 else -1, use_limits=True)
    if baseline == "scalar_prior_sample":
        return canonical_scalar_delta(state, params, 1 if rng.random() < positive_prior else -1, use_limits=True)
    if baseline == "uniform_signed":
        return uniform_signed_delta(state, params)
    if baseline == "nearest_contact":
        return nearest_contact_delta(state, params)
    if baseline == "noisy_signed_margin":
        return noisy_signed_delta(state, params, rng, noise_scale)
    raise ValueError(f"unknown baseline {baseline}")


def make_row(
    suite: str,
    baseline: str,
    seed: int,
    case_id: int,
    params: LinearContactParams,
    state: LinearContactState,
    field: Projection,
    repair: Projection,
    positive_prior: float,
    noise_scale: float,
    mask_rate: float,
    limit_scale: float,
) -> dict[str, float | int | str]:
    repaired = apply_delta(state, repair.delta)
    e0 = error_coordinate(state, params)
    field_effort = effort(field.delta, params.costs) if field.feasible else math.nan
    repair_effort = effort(repair.delta, params.costs)
    disagreement = math.sqrt(sum((a - b) * (a - b) for a, b in zip(repair.delta, field.delta))) if field.feasible else math.nan
    direction = dot(params.weights, repair.delta)
    correct = 1.0 if direction == 0.0 else float(math.copysign(1.0, direction) == math.copysign(1.0, e0))
    return {
        "suite": suite,
        "baseline": baseline,
        "seed": seed,
        "case_id": case_id,
        "contact_count": len(params.weights),
        "positive_prior": positive_prior,
        "noise_scale": noise_scale,
        "mask_rate": mask_rate,
        "limit_scale": limit_scale,
        "active_count": sum(1 for flag in params.active if flag),
        "error_sign": 1 if e0 >= 0.0 else -1,
        "initial_error": e0,
        "initial_margin": margin(state, params),
        "field_feasible": float(field.feasible),
        "success": float(is_success(repaired, params)),
        "post_margin": margin(repaired, params) if in_limits(repaired, params) else -999.0,
        "effort": repair_effort,
        "field_effort": field_effort,
        "disagreement_l2": disagreement,
        "correct_direction": correct,
        "clipped": float(repair.clipped or not repair.feasible),
    }


def write_rows(path: Path, rows: Iterable[dict[str, float | int | str]]) -> int:
    count = 0
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
            count += 1
    return count


def run_suite(
    path: Path,
    suite: str,
    seed: int,
    configs: list[dict[str, float | int | bool]],
    baselines: list[str],
) -> int:
    rng = random.Random(seed)

    def rows() -> Iterable[dict[str, float | int | str]]:
        case_id = 0
        for cfg in configs:
            local_seed = int(cfg["seed"])
            local_rng = random.Random(seed * 1000003 + local_seed)
            for _ in range(int(cfg["cases"])):
                params = random_params(
                    local_rng,
                    int(cfg["contact_count"]),
                    mask_rate=float(cfg.get("mask_rate", 0.0)),
                    limit_scale=float(cfg.get("limit_scale", 1.0)),
                    cost_spread=float(cfg.get("cost_spread", 1.0)),
                )
                state = sample_case(
                    local_rng,
                    params,
                    positive_prior=float(cfg.get("positive_prior", 0.5)),
                    near_limits=bool(cfg.get("near_limits", False)),
                    require_field_feasible=bool(cfg.get("require_field_feasible", True)),
                )
                field = true_field(state, params, use_limits=True)
                for baseline in baselines:
                    repair = repair_for_baseline(
                        baseline,
                        state,
                        params,
                        rng,
                        float(cfg.get("positive_prior", 0.5)),
                        float(cfg.get("noise_scale", 0.0)),
                    )
                    yield make_row(
                        suite,
                        baseline,
                        local_seed,
                        case_id,
                        params,
                        state,
                        field,
                        repair,
                        float(cfg.get("positive_prior", 0.5)),
                        float(cfg.get("noise_scale", 0.0)),
                        float(cfg.get("mask_rate", 0.0)),
                        float(cfg.get("limit_scale", 1.0)),
                    )
                case_id += 1

    return write_rows(path, rows())


def make_configs() -> dict[str, tuple[list[dict[str, float | int | bool]], list[str]]]:
    configs: dict[str, tuple[list[dict[str, float | int | bool]], list[str]]] = {}
    linear = []
    for contact_count in [2, 3, 4, 6]:
        for seed in range(12):
            linear.append({"seed": seed + 100 * contact_count, "contact_count": contact_count, "cases": 140})
    configs["linear_contact_grid"] = (linear, BASELINES)

    biased = []
    for positive_prior in [0.50, 0.65, 0.80, 0.90, 0.95]:
        for seed in range(12):
            biased.append({"seed": seed + int(1000 * positive_prior), "contact_count": 4, "cases": 150, "positive_prior": positive_prior})
    configs["biased_scalar_grid"] = (biased, ["scalar_random_sign", "scalar_global_sign", "scalar_prior_sample", "signed_margin", "counterfactual_field"])

    masks = []
    for mask_rate in [0.0, 0.2, 0.4]:
        for limit_scale in [0.45, 0.65, 0.90, 1.15]:
            for seed in range(8):
                masks.append(
                    {
                        "seed": seed + int(mask_rate * 100) + int(limit_scale * 1000),
                        "contact_count": 5,
                        "cases": 120,
                        "mask_rate": mask_rate,
                        "limit_scale": limit_scale,
                        "near_limits": True,
                        "require_field_feasible": False,
                    }
                )
    configs["mask_limit_grid"] = (masks, ["no_repair", "uniform_signed", "nearest_contact", "signed_margin", "counterfactual_field"])

    noise = []
    for noise_scale in [0.0, 0.02, 0.05, 0.10, 0.20, 0.35]:
        for seed in range(10):
            noise.append({"seed": seed + int(1000 * noise_scale), "contact_count": 4, "cases": 150, "noise_scale": noise_scale})
    configs["noise_mismatch_grid"] = (noise, ["scalar_random_sign", "noisy_signed_margin", "signed_margin", "counterfactual_field"])

    stress = []
    for seed in range(48):
        stress.append(
            {
                "seed": 5000 + seed,
                "contact_count": [2, 3, 4, 5, 6][seed % 5],
                "cases": 125,
                "positive_prior": [0.50, 0.65, 0.80, 0.90][seed % 4],
                "noise_scale": [0.0, 0.02, 0.05, 0.10][seed % 4],
                "mask_rate": [0.0, 0.1, 0.25][seed % 3],
                "limit_scale": [0.65, 0.90, 1.15][seed % 3],
                "near_limits": seed % 3 == 0,
                "require_field_feasible": False,
            }
        )
    configs["large_seed_stress"] = (stress, BASELINES)
    return configs


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def group_metrics(rows: list[dict[str, str]]) -> dict[str, float]:
    n = len(rows)
    if n == 0:
        return {}
    successes = [float(r["success"]) for r in rows]
    pos = [float(r["success"]) for r in rows if int(float(r["error_sign"])) > 0]
    neg = [float(r["success"]) for r in rows if int(float(r["error_sign"])) < 0]
    field_feasible = [float(r["field_feasible"]) for r in rows]
    efforts = [float(r["effort"]) for r in rows]
    margins = [float(r["post_margin"]) for r in rows if float(r["post_margin"]) > -998.0]
    disagreements = [float(r["disagreement_l2"]) for r in rows if r["disagreement_l2"] not in ("", "nan") and math.isfinite(float(r["disagreement_l2"]))]
    pos_success = sum(pos) / len(pos) if pos else math.nan
    neg_success = sum(neg) / len(neg) if neg else math.nan
    return {
        "n": float(n),
        "success": sum(successes) / n,
        "positive_success": pos_success,
        "negative_success": neg_success,
        "balanced_success": (pos_success + neg_success) / 2.0 if pos and neg else math.nan,
        "worst_group_success": min(pos_success, neg_success) if pos and neg else math.nan,
        "field_infeasible_rate": 1.0 - sum(field_feasible) / n,
        "mean_effort": sum(efforts) / n,
        "mean_post_margin": sum(margins) / len(margins) if margins else math.nan,
        "mean_disagreement": sum(disagreements) / len(disagreements) if disagreements else math.nan,
        "clipped_rate": sum(float(r["clipped"]) for r in rows) / n,
    }


def write_leaderboard(paths: list[Path]) -> list[dict[str, float | str]]:
    all_rows: list[dict[str, str]] = []
    for path in paths:
        all_rows.extend(load_csv(path))
    out: list[dict[str, float | str]] = []
    suites = sorted({r["suite"] for r in all_rows})
    for suite in suites:
        for baseline in BASELINES:
            subset = [r for r in all_rows if r["suite"] == suite and r["baseline"] == baseline]
            if not subset:
                continue
            m = group_metrics(subset)
            row: dict[str, float | str] = {"suite": suite, "baseline": baseline}
            row.update(m)
            out.append(row)
    with (RESULTS / "leaderboard.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        writer.writeheader()
        writer.writerows(out)
    return out


def tex_name(value: str) -> str:
    return value.replace("_", " ")


def write_tables(leaderboard: list[dict[str, float | str]], paths: list[Path]) -> None:
    key_rows = [
        r for r in leaderboard
        if r["suite"] in {"linear_contact_grid", "biased_scalar_grid", "mask_limit_grid", "noise_mismatch_grid", "large_seed_stress"}
        and r["baseline"] in {"scalar_random_sign", "scalar_global_sign", "noisy_signed_margin", "signed_margin", "counterfactual_field", "nearest_contact", "uniform_signed"}
    ]
    with (PAPER_TABLES / "full_scale_leaderboard.tex").open("w", encoding="utf-8") as f:
        f.write("\\begin{tabular}{llrrrrr}\\toprule\n")
        f.write("Suite & Baseline & $n$ & Success & Bal. & Worst & Effort\\\\\n")
        f.write("\\midrule\n")
        for r in key_rows:
            f.write(
                f"{tex_name(str(r['suite']))} & {tex_name(str(r['baseline']))} & {int(float(r['n']))} & "
                f"{100.0 * float(r['success']):.1f}\\% & {100.0 * float(r['balanced_success']):.1f}\\% & "
                f"{100.0 * float(r['worst_group_success']):.1f}\\% & {float(r['mean_effort']):.2f}\\\\\n"
            )
        f.write("\\bottomrule\\end{tabular}\n")

    biased_rows = load_csv(RESULTS / "biased_scalar_grid.csv")
    with (PAPER_TABLES / "bias_worst_group_table.tex").open("w", encoding="utf-8") as f:
        f.write("\\begin{tabular}{lrrrr}\\toprule\n")
        f.write("Baseline & Prior & Success & Bal. & Worst\\\\\n")
        f.write("\\midrule\n")
        for prior in [0.50, 0.65, 0.80, 0.90, 0.95]:
            for baseline in ["scalar_global_sign", "scalar_prior_sample", "signed_margin", "counterfactual_field"]:
                subset = [r for r in biased_rows if abs(float(r["positive_prior"]) - prior) < 1e-9 and r["baseline"] == baseline]
                m = group_metrics(subset)
                f.write(
                    f"{tex_name(baseline)} & {prior:.2f} & {100.0 * m['success']:.1f}\\% & "
                    f"{100.0 * m['balanced_success']:.1f}\\% & {100.0 * m['worst_group_success']:.1f}\\%\\\\\n"
                )
        f.write("\\bottomrule\\end{tabular}\n")

    noise_rows = load_csv(RESULTS / "noise_mismatch_grid.csv")
    with (PAPER_TABLES / "noise_boundary_table.tex").open("w", encoding="utf-8") as f:
        f.write("\\begin{tabular}{lrrrr}\\toprule\n")
        f.write("Baseline & Noise & Success & Effort & Margin\\\\\n")
        f.write("\\midrule\n")
        for noise in [0.0, 0.02, 0.05, 0.10, 0.20, 0.35]:
            for baseline in ["scalar_random_sign", "noisy_signed_margin", "signed_margin", "counterfactual_field"]:
                subset = [r for r in noise_rows if abs(float(r["noise_scale"]) - noise) < 1e-9 and r["baseline"] == baseline]
                m = group_metrics(subset)
                f.write(
                    f"{tex_name(baseline)} & {noise:.2f} & {100.0 * m['success']:.1f}\\% & "
                    f"{m['mean_effort']:.2f} & {m['mean_post_margin']:.2f}\\\\\n"
                )
        f.write("\\bottomrule\\end{tabular}\n")

    mask_rows = load_csv(RESULTS / "mask_limit_grid.csv")
    with (PAPER_TABLES / "mask_feasibility_table.tex").open("w", encoding="utf-8") as f:
        f.write("\\begin{tabular}{rrrrr}\\toprule\n")
        f.write("Mask & Limit & Field infeasible & Field success & Nearest success\\\\\n")
        f.write("\\midrule\n")
        for mask in [0.0, 0.2, 0.4]:
            for limit in [0.45, 0.65, 0.90, 1.15]:
                field_rows = [r for r in mask_rows if abs(float(r["mask_rate"]) - mask) < 1e-9 and abs(float(r["limit_scale"]) - limit) < 1e-9 and r["baseline"] == "counterfactual_field"]
                nearest_rows = [r for r in mask_rows if abs(float(r["mask_rate"]) - mask) < 1e-9 and abs(float(r["limit_scale"]) - limit) < 1e-9 and r["baseline"] == "nearest_contact"]
                fm = group_metrics(field_rows)
                nm = group_metrics(nearest_rows)
                f.write(
                    f"{mask:.1f} & {limit:.2f} & {100.0 * fm['field_infeasible_rate']:.1f}\\% & "
                    f"{100.0 * fm['success']:.1f}\\% & {100.0 * nm['success']:.1f}\\%\\\\\n"
                )
        f.write("\\bottomrule\\end{tabular}\n")

    with (PAPER_TABLES / "baseline_access_table.tex").open("w", encoding="utf-8") as f:
        f.write("\\begin{tabular}{lll}\\toprule\n")
        f.write("Baseline & Uses sign? & Uses contact allocation?\\\\\n")
        f.write("\\midrule\n")
        entries = [
            ("no repair", "no", "no"),
            ("scalar random sign", "guessed", "generic"),
            ("scalar global sign", "prior only", "generic"),
            ("uniform signed", "yes", "no"),
            ("nearest contact", "yes", "greedy"),
            ("noisy signed margin", "noisy", "estimated"),
            ("signed margin", "yes", "yes"),
            ("counterfactual field", "yes", "yes, constrained"),
        ]
        for name, sign, allocation in entries:
            f.write(f"{name} & {sign} & {allocation}\\\\\n")
        f.write("\\bottomrule\\end{tabular}\n")


def copy_figures(paths: Iterable[Path]) -> None:
    for path in paths:
        shutil.copy2(path, PAPER_FIGURES / path.name)


def plot_success_leaderboard(leaderboard: list[dict[str, float | str]]) -> Path:
    import matplotlib.pyplot as plt

    path = FIGURES / "full_scale_success_leaderboard.png"
    subset = [r for r in leaderboard if r["suite"] == "large_seed_stress"]
    subset = sorted(subset, key=lambda r: float(r["success"]))
    labels = [tex_name(str(r["baseline"])) for r in subset]
    success = [float(r["success"]) for r in subset]
    balanced = [float(r["balanced_success"]) for r in subset]
    x = range(len(labels))
    plt.figure(figsize=(8.2, 4.2))
    plt.bar([i - 0.18 for i in x], success, width=0.36, label="overall")
    plt.bar([i + 0.18 for i in x], balanced, width=0.36, label="balanced")
    plt.ylim(0, 1.05)
    plt.ylabel("one-step repair success")
    plt.xticks(list(x), labels, rotation=30, ha="right", fontsize=8)
    plt.title("Large stress suite: scalar labels versus contact fields")
    plt.legend(frameon=False)
    plt.tight_layout()
    plt.savefig(path, dpi=220)
    plt.close()
    return path


def plot_bias_curve(rows: list[dict[str, str]]) -> Path:
    import matplotlib.pyplot as plt

    path = FIGURES / "bias_worst_group_curve.png"
    baselines = ["scalar_random_sign", "scalar_global_sign", "scalar_prior_sample", "signed_margin", "counterfactual_field"]
    priors = sorted({float(r["positive_prior"]) for r in rows})
    plt.figure(figsize=(7.0, 4.0))
    for baseline in baselines:
        ys = []
        for prior in priors:
            subset = [r for r in rows if r["baseline"] == baseline and abs(float(r["positive_prior"]) - prior) < 1e-9]
            ys.append(group_metrics(subset)["worst_group_success"])
        plt.plot(priors, ys, marker="o", label=tex_name(baseline))
    plt.xlabel("positive repair-sign prior")
    plt.ylabel("worst-group success")
    plt.ylim(0, 1.05)
    plt.title("Majority scalar repair hides minority-direction failure")
    plt.grid(True, alpha=0.25)
    plt.legend(frameon=False, fontsize=8)
    plt.tight_layout()
    plt.savefig(path, dpi=220)
    plt.close()
    return path


def plot_noise(rows: list[dict[str, str]]) -> Path:
    import matplotlib.pyplot as plt

    path = FIGURES / "noise_mismatch_success.png"
    baselines = ["scalar_random_sign", "noisy_signed_margin", "signed_margin", "counterfactual_field"]
    levels = sorted({float(r["noise_scale"]) for r in rows})
    plt.figure(figsize=(7.0, 4.0))
    for baseline in baselines:
        ys = []
        for level in levels:
            subset = [r for r in rows if r["baseline"] == baseline and abs(float(r["noise_scale"]) - level) < 1e-9]
            ys.append(group_metrics(subset)["success"])
        plt.plot(levels, ys, marker="o", label=tex_name(baseline))
    plt.xlabel("relative margin/weight noise")
    plt.ylabel("one-step success")
    plt.ylim(0, 1.05)
    plt.title("Signed margins degrade under contact/margin noise")
    plt.grid(True, alpha=0.25)
    plt.legend(frameon=False, fontsize=8)
    plt.tight_layout()
    plt.savefig(path, dpi=220)
    plt.close()
    return path


def plot_mask(rows: list[dict[str, str]]) -> Path:
    import matplotlib.pyplot as plt

    path = FIGURES / "mask_limit_feasibility_map.png"
    masks = sorted({float(r["mask_rate"]) for r in rows})
    limits = sorted({float(r["limit_scale"]) for r in rows})
    mat = []
    for mask in masks:
        row = []
        for limit in limits:
            subset = [
                r for r in rows
                if r["baseline"] == "counterfactual_field"
                and abs(float(r["mask_rate"]) - mask) < 1e-9
                and abs(float(r["limit_scale"]) - limit) < 1e-9
            ]
            row.append(group_metrics(subset)["field_infeasible_rate"])
        mat.append(row)
    plt.figure(figsize=(5.6, 3.8))
    plt.imshow(mat, cmap="magma", vmin=0.0, vmax=1.0, aspect="auto")
    plt.colorbar(label="field infeasible rate")
    plt.xticks(range(len(limits)), [f"{v:.2f}" for v in limits])
    plt.yticks(range(len(masks)), [f"{v:.1f}" for v in masks])
    plt.xlabel("finger travel limit scale")
    plt.ylabel("contact mask rate")
    plt.title("Executable fields expose infeasible repair cases")
    plt.tight_layout()
    plt.savefig(path, dpi=220)
    plt.close()
    return path


def plot_effort_pareto(leaderboard: list[dict[str, float | str]]) -> Path:
    import matplotlib.pyplot as plt

    path = FIGURES / "effort_success_pareto.png"
    subset = [r for r in leaderboard if r["suite"] == "large_seed_stress"]
    plt.figure(figsize=(6.4, 4.2))
    for r in subset:
        plt.scatter(float(r["mean_effort"]), float(r["balanced_success"]), s=70)
        plt.annotate(tex_name(str(r["baseline"])), (float(r["mean_effort"]), float(r["balanced_success"])), xytext=(4, 3), textcoords="offset points", fontsize=8)
    plt.xlabel("mean repair effort")
    plt.ylabel("balanced one-step success")
    plt.ylim(0, 1.05)
    plt.title("Repair effort versus balanced success")
    plt.grid(True, alpha=0.25)
    plt.tight_layout()
    plt.savefig(path, dpi=220)
    plt.close()
    return path


def summarize_outputs(csv_paths: list[Path]) -> list[Path]:
    leaderboard = write_leaderboard(csv_paths)
    write_tables(leaderboard, csv_paths)
    figures = [
        plot_success_leaderboard(leaderboard),
        plot_effort_pareto(leaderboard),
        plot_bias_curve(load_csv(RESULTS / "biased_scalar_grid.csv")),
        plot_noise(load_csv(RESULTS / "noise_mismatch_grid.csv")),
        plot_mask(load_csv(RESULTS / "mask_limit_grid.csv")),
    ]
    copy_figures(figures)
    return figures


def main() -> int:
    args = parse_args()
    ensure_dirs()
    configs = make_configs()
    csv_paths = [
        RESULTS / "linear_contact_grid.csv",
        RESULTS / "biased_scalar_grid.csv",
        RESULTS / "mask_limit_grid.csv",
        RESULTS / "noise_mismatch_grid.csv",
        RESULTS / "large_seed_stress.csv",
    ]
    if args.summarize_only:
        summarize_outputs(csv_paths)
        print("summarized existing full-scale field outputs")
        return 0

    suite_counts: dict[str, int] = {}
    total_rows = 0
    for index, (suite, (suite_configs, baselines)) in enumerate(configs.items()):
        path = RESULTS / f"{suite}.csv"
        count = run_suite(path, suite, args.seed + index * 97, suite_configs, baselines)
        suite_counts[path.name] = count
        total_rows += count
        print(f"wrote {path.name}: {count} baseline rows", flush=True)

    figures = summarize_outputs(csv_paths)
    summary = {
        "seed": args.seed,
        "suite_rows": suite_counts,
        "total_baseline_rows": total_rows,
        "streaming": True,
        "raw_trajectories_saved": False,
        "figure_count": len(figures),
        "claim_scope": "linearized contact-balance simulation; not hardware validation",
    }
    (RESULTS / "full_scale_summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
