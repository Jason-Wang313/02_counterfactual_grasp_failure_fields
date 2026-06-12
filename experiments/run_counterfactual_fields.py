from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
import random
import sys
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from cgff_mechanics import (  # noqa: E402
    GraspState,
    PinchParams,
    apply_field,
    counterfactual_failure_field,
    error_coordinate,
    failure_score,
    is_success,
    scalar_only_repair,
    stability_margin,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=20000)
    parser.add_argument("--seed", type=int, default=2)
    parser.add_argument("--out", type=Path, default=ROOT / "results")
    parser.add_argument("--stress-seeds", type=int, default=30)
    parser.add_argument("--stress-n", type=int, default=3000)
    return parser.parse_args()


def sample_state(rng: random.Random, params: PinchParams) -> GraspState:
    return GraspState(
        y_left=rng.uniform(-0.75, 0.75),
        y_right=rng.uniform(-0.75, 0.75),
        torque_over_normal=rng.uniform(-0.95, 0.95),
    )


def summarize(rows: List[Dict[str, float]]) -> Dict[str, float]:
    if not rows:
        return {}
    n = len(rows)
    exact_success = sum(r["field_success"] for r in rows) / n
    random_success = sum(r["scalar_random_success"] for r in rows) / n
    global_success = sum(r["scalar_global_success"] for r in rows) / n
    signed_success = sum(r["signed_margin_success"] for r in rows) / n
    no_repair_success = sum(r["no_repair_success"] for r in rows) / n
    one_step_gap = exact_success - random_success
    signs = [r["repair_sign"] for r in rows if r["repair_sign"] != 0]
    p_pos = sum(1 for s in signs if s > 0) / max(1, len(signs))
    if p_pos in (0.0, 1.0):
        sign_entropy = 0.0
    else:
        sign_entropy = -p_pos * math.log(p_pos, 2) - (1.0 - p_pos) * math.log(1.0 - p_pos, 2)
    return {
        "failed_feasible_cases": n,
        "counterfactual_field_one_step_success": exact_success,
        "scalar_random_sign_one_step_success": random_success,
        "scalar_global_sign_one_step_success": global_success,
        "signed_margin_projection_success": signed_success,
        "no_repair_success": no_repair_success,
        "field_minus_random_success": one_step_gap,
        "repair_sign_positive_fraction": p_pos,
        "repair_sign_entropy_bits": sign_entropy,
        "mean_field_l2": sum(r["field_l2"] for r in rows) / n,
        "mean_initial_margin": sum(r["initial_margin"] for r in rows) / n,
        "mean_failure_score": sum(r["failure_score"] for r in rows) / n,
    }


def write_csv(path: Path, rows: List[Dict[str, float]]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def make_same_score_pairs(params: PinchParams) -> List[Dict[str, float]]:
    pairs: List[Dict[str, float]] = []
    for abs_e in (params.stable_error_radius + 0.08, params.stable_error_radius + 0.18):
        for sign in (-1, 1):
            e = sign * abs_e
            state = GraspState(y_left=-0.10, y_right=0.10, torque_over_normal=0.20 + e)
            field = counterfactual_failure_field(state, params)
            pairs.append(
                {
                    "abs_error": abs_e,
                    "error_sign": sign,
                    "y_left": state.y_left,
                    "y_right": state.y_right,
                    "torque_over_normal": state.torque_over_normal,
                    "failure_score": failure_score(state, params),
                    "margin": stability_margin(state, params),
                    "dy_left": field.dy_left,
                    "dy_right": field.dy_right,
                    "delta_difference": field.delta_difference,
                    "repair_sign": field.repair_sign,
                }
            )
    return pairs


def sample_stress_params(rng: random.Random) -> PinchParams:
    for _ in range(100):
        params = PinchParams(
            half_width=rng.uniform(0.35, 0.75),
            normal_force=rng.uniform(0.70, 1.35),
            friction_coeff=rng.uniform(0.45, 0.95),
            weight=rng.uniform(0.35, 1.15),
            finger_y_limit=rng.uniform(0.75, 1.20),
        )
        if params.stable_error_radius > 0.05:
            return params
    return PinchParams()


def run_trial(n: int, seed: int, params: PinchParams) -> tuple[List[Dict[str, float]], Dict[str, float]]:
    rng = random.Random(seed)
    candidates: List[GraspState] = []
    while len(candidates) < n:
        state = sample_state(rng, params)
        field = counterfactual_failure_field(state, params)
        if field.margin_before < 0.0 and field.feasible_within_limits:
            candidates.append(state)

    positive_count = sum(
        1 for state in candidates if counterfactual_failure_field(state, params).repair_sign > 0
    )
    global_sign = 1 if positive_count >= len(candidates) / 2 else -1

    rows: List[Dict[str, float]] = []
    for idx, state in enumerate(candidates):
        field = counterfactual_failure_field(state, params)
        repaired = apply_field(state, field.dy_left, field.dy_right)

        random_sign = 1 if rng.random() >= 0.5 else -1
        signed_sign = 1 if error_coordinate(state) > 0.0 else -1
        rnd_left, rnd_right = scalar_only_repair(state, params, random_sign)
        glob_left, glob_right = scalar_only_repair(state, params, global_sign)
        signed_left, signed_right = scalar_only_repair(state, params, signed_sign)

        random_repaired = apply_field(state, rnd_left, rnd_right)
        global_repaired = apply_field(state, glob_left, glob_right)
        signed_repaired = apply_field(state, signed_left, signed_right)

        rows.append(
            {
                "case_id": idx,
                "y_left": state.y_left,
                "y_right": state.y_right,
                "torque_over_normal": state.torque_over_normal,
                "initial_margin": field.margin_before,
                "failure_score": failure_score(state, params),
                "dy_left": field.dy_left,
                "dy_right": field.dy_right,
                "delta_difference": field.delta_difference,
                "repair_sign": field.repair_sign,
                "field_l2": field.l2_norm,
                "field_success": float(is_success(repaired, params)),
                "scalar_random_success": float(is_success(random_repaired, params)),
                "scalar_global_success": float(is_success(global_repaired, params)),
                "signed_margin_success": float(is_success(signed_repaired, params)),
                "no_repair_success": float(is_success(state, params)),
            }
        )

    summary = summarize(rows)
    summary.update(
        {
            "seed": seed,
            "requested_cases": n,
            "stable_error_radius": params.stable_error_radius,
            "global_scalar_sign_guess": global_sign,
            "half_width": params.half_width,
            "normal_force": params.normal_force,
            "friction_coeff": params.friction_coeff,
            "weight": params.weight,
            "finger_y_limit": params.finger_y_limit,
        }
    )
    return rows, summary


def summarize_stress(items: List[Dict[str, float]]) -> Dict[str, float]:
    if not items:
        return {}
    keys = [
        "counterfactual_field_one_step_success",
        "scalar_random_sign_one_step_success",
        "scalar_global_sign_one_step_success",
        "signed_margin_projection_success",
        "repair_sign_entropy_bits",
        "field_minus_random_success",
    ]
    out: Dict[str, float] = {"stress_seed_count": float(len(items))}
    for key in keys:
        vals = [float(item[key]) for item in items]
        mean = sum(vals) / len(vals)
        if len(vals) > 1:
            var = sum((v - mean) ** 2 for v in vals) / (len(vals) - 1)
            ci95 = 1.96 * math.sqrt(var) / math.sqrt(len(vals))
        else:
            ci95 = 0.0
        out[f"{key}_mean"] = mean
        out[f"{key}_ci95"] = ci95
        out[f"{key}_min"] = min(vals)
        out[f"{key}_max"] = max(vals)
    return out


def maybe_plot_stress(results_dir: Path, items: List[Dict[str, float]]) -> str:
    try:
        import matplotlib.pyplot as plt
    except Exception as exc:  # pragma: no cover - environment dependent
        return f"matplotlib unavailable: {exc}"

    labels = ["scalar random", "scalar global", "signed margin", "failure field"]
    keys = [
        "scalar_random_sign_one_step_success",
        "scalar_global_sign_one_step_success",
        "signed_margin_projection_success",
        "counterfactual_field_one_step_success",
    ]
    means: List[float] = []
    cis: List[float] = []
    for key in keys:
        vals = [float(item[key]) for item in items]
        mean = sum(vals) / len(vals)
        if len(vals) > 1:
            var = sum((v - mean) ** 2 for v in vals) / (len(vals) - 1)
            ci95 = 1.96 * math.sqrt(var) / math.sqrt(len(vals))
        else:
            ci95 = 0.0
        means.append(mean)
        cis.append(ci95)

    plt.figure(figsize=(6.2, 3.7))
    plt.bar(labels, means, yerr=cis, capsize=4, color=["#7873b8", "#bd8b2d", "#4d78a8", "#0b6f6a"])
    plt.ylim(0, 1.05)
    plt.ylabel("mean one-step repair success")
    plt.title("30-seed parameter stress")
    plt.xticks(rotation=15, ha="right")
    plt.tight_layout()
    plt.savefig(results_dir / "stress_success_rates.png", dpi=220)
    plt.close()
    return "stress plot written"


def run_stress(results_dir: Path, stress_seeds: int, stress_n: int) -> Dict[str, float]:
    rows: List[Dict[str, float]] = []
    for stress_idx in range(stress_seeds):
        rng = random.Random(10000 + stress_idx)
        params = sample_stress_params(rng)
        _, summary = run_trial(stress_n, 20000 + stress_idx, params)
        summary["stress_index"] = stress_idx
        rows.append(summary)
    write_csv(results_dir / "seed_stress_summary.csv", rows)
    plot_status = maybe_plot_stress(results_dir, rows)
    aggregate = summarize_stress(rows)
    aggregate["plot_status"] = plot_status
    with (results_dir / "stress_summary.json").open("w", encoding="utf-8") as f:
        json.dump(aggregate, f, indent=2, sort_keys=True)
    return aggregate


def maybe_plot(results_dir: Path, rows: List[Dict[str, float]], pairs: List[Dict[str, float]], summary: Dict[str, float]) -> str:
    try:
        import matplotlib.pyplot as plt
    except Exception as exc:  # pragma: no cover - environment dependent
        return f"matplotlib unavailable: {exc}"

    scores = [r["failure_score"] for r in rows[:4000]]
    repairs = [r["delta_difference"] for r in rows[:4000]]
    colors = ["#0b6f6a" if r > 0 else "#b13f2e" for r in repairs]
    plt.figure(figsize=(6.0, 3.8))
    plt.scatter(scores, repairs, s=10, alpha=0.35, c=colors, linewidths=0)
    plt.axhline(0.0, color="black", linewidth=0.8)
    plt.xlabel("scalar failure score")
    plt.ylabel("counterfactual change in y_R - y_L")
    plt.title("Same scalar failure scores can require opposite contact edits")
    plt.tight_layout()
    plt.savefig(results_dir / "same_score_opposite_repairs.png", dpi=220)
    plt.close()

    labels = [
        "no repair",
        "scalar global sign",
        "scalar random sign",
        "signed margin",
        "failure field",
    ]
    values = [
        summary["no_repair_success"],
        summary["scalar_global_sign_one_step_success"],
        summary["scalar_random_sign_one_step_success"],
        summary["signed_margin_projection_success"],
        summary["counterfactual_field_one_step_success"],
    ]
    plt.figure(figsize=(6.0, 3.7))
    plt.bar(labels, values, color=["#777777", "#bd8b2d", "#7873b8", "#4d78a8", "#0b6f6a"])
    plt.ylim(0, 1.05)
    plt.ylabel("one-step repair success")
    plt.xticks(rotation=15, ha="right")
    plt.tight_layout()
    plt.savefig(results_dir / "repair_success_rates.png", dpi=220)
    plt.close()

    plt.figure(figsize=(5.2, 4.6))
    for row in pairs:
        plt.scatter(row["y_left"], row["y_right"], color="#333333")
        plt.arrow(
            row["y_left"],
            row["y_right"],
            row["dy_left"],
            row["dy_right"],
            color="#0b6f6a" if row["repair_sign"] > 0 else "#b13f2e",
            width=0.003,
            length_includes_head=True,
        )
    plt.xlabel("left contact height")
    plt.ylabel("right contact height")
    plt.title("Counterfactual field arrows for same-score failures")
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig(results_dir / "pair_failure_fields.png", dpi=220)
    plt.close()

    return "plots written"


def main() -> int:
    args = parse_args()
    params = PinchParams()
    args.out.mkdir(parents=True, exist_ok=True)

    rows, summary = run_trial(args.n, args.seed, params)
    pairs = make_same_score_pairs(params)
    summary.update(
        {
            "same_score_pair_count": len(pairs),
            "claim_scope": "2D quasi-static pinch counterexample; not a real-robot validation",
        }
    )
    stress_summary = run_stress(args.out, args.stress_seeds, args.stress_n)

    write_csv(args.out / "counterfactual_field_cases.csv", rows)
    write_csv(args.out / "same_score_pairs.csv", pairs)
    plot_status = maybe_plot(args.out, rows, pairs, summary)
    summary["plot_status"] = plot_status
    summary["stress_summary_file"] = "stress_summary.json"
    summary["seed_stress_summary_file"] = "seed_stress_summary.csv"
    summary["stress_field_success_mean"] = stress_summary.get("counterfactual_field_one_step_success_mean", 0.0)
    summary["stress_scalar_random_success_mean"] = stress_summary.get("scalar_random_sign_one_step_success_mean", 0.0)

    with (args.out / "counterfactual_field_summary.json").open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, sort_keys=True)

    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
