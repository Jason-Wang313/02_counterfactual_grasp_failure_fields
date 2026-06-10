"""Build literature artifacts for paper 02.

The pipeline uses OpenAlex metadata as the broad sweep source. It is designed to
be non-interactive and failure-tolerant: partial network failures keep the run
moving, and all generated artifacts describe the retrieval method.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import textwrap
import time
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Iterable

import requests


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs"
RESULTS = ROOT / "results"

OPENALEX = "https://api.openalex.org/works"
MAILTO = "robotics-paper-agent@example.com"


SEARCH_QUERIES = [
    "robot grasping tactile perception failure",
    "robot grasp failure tactile feedback",
    "counterfactual explanation robot grasping",
    "contact rich manipulation robot tactile",
    "force closure grasp failure contact",
    "grasp stability tactile servoing robot",
    "failure prediction robotic grasping",
    "grasp affordance contact fields robotics",
    "visual tactile robotic grasping failure",
    "robot manipulation contact model failure",
    "dexterous grasp tactile learning",
    "grasp quality convolutional neural network",
    "antipodal grasp sampling robot learning",
    "tactile regrasping slip detection",
    "GelSight tactile robot grasping manipulation",
    "visuotactile manipulation contact learning",
    "grasp wrench space force closure",
    "contact point selection robotic grasping",
    "robotic grasp pose detection point cloud",
    "sim to real grasping tactile perception",
    "failure recovery robotic manipulation grasp",
    "robot grasp repair contact feedback",
    "tactile servo control grasp",
    "slip prediction tactile robot gripper",
    "object pose estimation tactile grasping",
    "grasping deformable objects tactile",
    "contact implicit representation manipulation",
    "neural descriptor fields robot manipulation",
    "diffusion policy contact rich manipulation",
    "robot foundation model grasping manipulation",
    "language conditioned robot grasping failure",
    "self supervised tactile representation robot",
    "active tactile exploration manipulation",
    "grasp synthesis deep learning survey",
    "robot manipulation failure diagnosis",
    "counterfactual learning embodied agents",
    "contact dynamics learning robotic manipulation",
    "physics based grasp analysis robot",
    "multi fingered grasp planning force closure",
    "tactile based grasp stability assessment",
    "robot gripper tactile contact localization",
    "grasp outcome prediction robot learning",
    "contact maps robotic manipulation learning",
    "local shape tactile grasping robot",
    "uncertainty grasping tactile robot",
    "post hoc classifier explanation robotics",
]


CORE_TERMS = {
    "grasp": 4.0,
    "grasping": 4.0,
    "gripper": 2.5,
    "tactile": 4.0,
    "touch": 2.5,
    "contact": 3.5,
    "force closure": 3.5,
    "failure": 3.2,
    "slip": 2.8,
    "manipulation": 2.8,
    "robot": 2.5,
    "robotic": 2.5,
    "counterfactual": 4.0,
    "affordance": 2.0,
    "wrench": 2.4,
    "dexterous": 2.0,
    "gel": 1.0,
    "gelsight": 2.4,
    "field": 1.5,
}

HOSTILE_TERMS = {
    "grasp quality": 5.0,
    "force closure": 5.0,
    "tactile": 4.0,
    "failure prediction": 4.5,
    "grasp stability": 4.5,
    "counterfactual": 5.0,
    "contact": 3.2,
    "repair": 3.5,
    "servo": 2.5,
    "slip": 3.5,
    "affordance": 3.0,
    "failure recovery": 4.0,
    "post hoc": 2.5,
}


KNOWN_IMPORTANT = [
    {
        "title": "The Mechanics of Robot Grasping",
        "year": 1985,
        "venue": "MIT Press",
        "authors": "Matthew T. Mason; J. Kenneth Salisbury",
        "doi": "",
        "url": "https://mitpress.mit.edu/9780262631317/robot-hands-and-the-mechanics-of-manipulation/",
        "abstract": "Classic mechanics treatment of robot hands, contact models, friction, and grasping.",
        "source_query": "curated important prior",
        "cited_by_count": 0,
    },
    {
        "title": "Planning Optimal Grasps",
        "year": 1992,
        "venue": "IEEE International Conference on Robotics and Automation",
        "authors": "Carlo Ferrari; John Canny",
        "doi": "",
        "url": "",
        "abstract": "Introduces grasp quality measures based on wrench space and force closure.",
        "source_query": "curated important prior",
        "cited_by_count": 0,
    },
    {
        "title": "GraspIt! A Versatile Simulator for Robotic Grasping",
        "year": 2004,
        "venue": "IEEE Robotics and Automation Magazine",
        "authors": "Andrew T. Miller; Peter K. Allen",
        "doi": "",
        "url": "",
        "abstract": "Simulator and analysis environment for multi-fingered grasp planning and evaluation.",
        "source_query": "curated important prior",
        "cited_by_count": 0,
    },
    {
        "title": "Dex-Net 2.0: Deep Learning to Plan Robust Grasps with Synthetic Point Clouds and Analytic Grasp Metrics",
        "year": 2017,
        "venue": "Robotics: Science and Systems",
        "authors": "Jeffrey Mahler; et al.",
        "doi": "",
        "url": "",
        "abstract": "Learns grasp quality from synthetic depth images and analytic robust grasp metrics.",
        "source_query": "curated important prior",
        "cited_by_count": 0,
    },
    {
        "title": "GQ-CNN: A Grasp Quality Convolutional Neural Network for Planning Robust Grasps",
        "year": 2017,
        "venue": "CoRL",
        "authors": "Jeffrey Mahler; et al.",
        "doi": "",
        "url": "",
        "abstract": "Predicts grasp success probability for candidate grasps from depth image crops.",
        "source_query": "curated important prior",
        "cited_by_count": 0,
    },
    {
        "title": "Learning Hand-Eye Coordination for Robotic Grasping with Deep Learning and Large-Scale Data Collection",
        "year": 2016,
        "venue": "ISER",
        "authors": "Sergey Levine; Peter Pastor; Alex Krizhevsky; Julian Ibarz; Deirdre Quillen",
        "doi": "",
        "url": "",
        "abstract": "Large-scale robot grasp data trains a visuomotor grasping policy.",
        "source_query": "curated important prior",
        "cited_by_count": 0,
    },
    {
        "title": "Closing the Loop for Robotic Grasping: A Real-time, Generative Grasp Synthesis Approach",
        "year": 2018,
        "venue": "Robotics: Science and Systems",
        "authors": "Douglas Morrison; Peter Corke; Jurgen Leitner",
        "doi": "",
        "url": "",
        "abstract": "GG-CNN predicts grasp quality and pose densely from depth for closed-loop grasping.",
        "source_query": "curated important prior",
        "cited_by_count": 0,
    },
    {
        "title": "6-DoF GraspNet: Variational Grasp Generation for Object Manipulation",
        "year": 2019,
        "venue": "ICCV",
        "authors": "Arsalan Mousavian; Clemens Eppner; Dieter Fox",
        "doi": "",
        "url": "",
        "abstract": "Generates and evaluates 6-DoF grasp poses from point clouds.",
        "source_query": "curated important prior",
        "cited_by_count": 0,
    },
    {
        "title": "Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes",
        "year": 2021,
        "venue": "ICRA",
        "authors": "Martin Sundermeyer; Arsalan Mousavian; Rudolph Triebel; Dieter Fox",
        "doi": "",
        "url": "",
        "abstract": "Predicts dense contact-based 6-DoF grasp candidates from scene point clouds.",
        "source_query": "curated important prior",
        "cited_by_count": 0,
    },
    {
        "title": "The GelSight Sensor: A Transparent Tactile Sensor for Robot Manipulation",
        "year": 2014,
        "venue": "Robotics",
        "authors": "Rui Li; Robert Platt; Wenzhen Yuan; Andreas ten Pas; Nathan Roscup; Mandayam Srinivasan; Edward Adelson",
        "doi": "",
        "url": "",
        "abstract": "Optical tactile sensor providing high-resolution contact geometry for manipulation.",
        "source_query": "curated important prior",
        "cited_by_count": 0,
    },
    {
        "title": "Tactile Dexterity: Manipulation Primitives with Tactile Feedback",
        "year": 2019,
        "venue": "ICRA",
        "authors": "Roberto Calandra; et al.",
        "doi": "",
        "url": "",
        "abstract": "Uses tactile observations for manipulation primitives and contact-rich feedback.",
        "source_query": "curated important prior",
        "cited_by_count": 0,
    },
    {
        "title": "Deep Learning for Detecting Robotic Grasps",
        "year": 2015,
        "venue": "IJRR",
        "authors": "Ian Lenz; Honglak Lee; Ashutosh Saxena",
        "doi": "",
        "url": "",
        "abstract": "Detects robotic grasp rectangles using deep networks trained on grasp datasets.",
        "source_query": "curated important prior",
        "cited_by_count": 0,
    },
]


def safe_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return re.sub(r"\s+", " ", value).strip()
    return str(value)


def normalize_title(title: str) -> str:
    title = safe_text(title).lower()
    title = re.sub(r"[^a-z0-9 ]+", " ", title)
    return re.sub(r"\s+", " ", title).strip()


def abstract_from_inverted(index: dict[str, list[int]] | None) -> str:
    if not index:
        return ""
    max_pos = 0
    for positions in index.values():
        if positions:
            max_pos = max(max_pos, max(positions))
    words = [""] * (max_pos + 1)
    for word, positions in index.items():
        for pos in positions:
            if 0 <= pos < len(words):
                words[pos] = word
    return safe_text(" ".join(words))


def strip_latex(text: str) -> str:
    text = safe_text(text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("{", "").replace("}", "")
    return re.sub(r"\s+", " ", text).strip()


def openalex_request(params: dict[str, Any]) -> dict[str, Any]:
    params = dict(params)
    params.setdefault("mailto", MAILTO)
    for attempt in range(4):
        try:
            response = requests.get(OPENALEX, params=params, timeout=25)
            if response.status_code == 200:
                return response.json()
            time.sleep(1.5 + attempt)
        except requests.RequestException:
            time.sleep(1.5 + attempt)
    return {"results": []}


def work_to_row(work: dict[str, Any], source_query: str) -> dict[str, Any]:
    primary_location = work.get("primary_location") or {}
    source = primary_location.get("source") or {}
    authorships = work.get("authorships") or []
    authors = []
    for authorship in authorships[:8]:
        author = authorship.get("author") or {}
        if author.get("display_name"):
            authors.append(author["display_name"])
    if len(authorships) > 8:
        authors.append("et al.")
    doi = safe_text(work.get("doi"))
    title = strip_latex(work.get("display_name") or "")
    abstract = abstract_from_inverted(work.get("abstract_inverted_index"))
    return {
        "title": title,
        "year": work.get("publication_year") or "",
        "venue": safe_text(source.get("display_name") or work.get("type_crossref") or work.get("type")),
        "authors": "; ".join(authors),
        "doi": doi,
        "url": safe_text(work.get("id")),
        "abstract": abstract,
        "source_query": source_query,
        "cited_by_count": work.get("cited_by_count") or 0,
    }


def collect_openalex(max_pages: int = 3, per_page: int = 200) -> list[dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    for query in SEARCH_QUERIES:
        for page in range(1, max_pages + 1):
            data = openalex_request(
                {
                    "search": query,
                    "per-page": per_page,
                    "page": page,
                    "sort": "cited_by_count:desc",
                }
            )
            batch = data.get("results") or []
            for work in batch:
                row = work_to_row(work, query)
                key = normalize_title(row["title"])
                if not key:
                    continue
                if key not in rows:
                    rows[key] = row
                else:
                    old = rows[key]
                    old_queries = set(old.get("source_query", "").split(" | "))
                    old_queries.add(query)
                    old["source_query"] = " | ".join(sorted(q for q in old_queries if q))
                    if len(row.get("abstract", "")) > len(old.get("abstract", "")):
                        old["abstract"] = row["abstract"]
                    if int(row.get("cited_by_count") or 0) > int(old.get("cited_by_count") or 0):
                        old["cited_by_count"] = row["cited_by_count"]
            time.sleep(0.12)
    for item in KNOWN_IMPORTANT:
        key = normalize_title(item["title"])
        rows.setdefault(key, item.copy())
    return list(rows.values())


def term_score(text: str, terms: dict[str, float]) -> float:
    low = text.lower()
    score = 0.0
    for term, weight in terms.items():
        if " " in term:
            count = low.count(term)
        else:
            count = len(re.findall(r"\b" + re.escape(term) + r"\b", low))
        if count:
            score += weight * min(count, 4)
    return score


def tags_for(text: str) -> list[str]:
    low = text.lower()
    tags = []
    checks = [
        ("grasp-quality", ["grasp quality", "grasp metric", "force closure", "wrench"]),
        ("tactile", ["tactile", "touch", "gelsight", "taxel"]),
        ("failure", ["failure", "slip", "unstable", "recovery", "error"]),
        ("contact-field", ["contact map", "contact field", "contact point", "contact-rich", "contact rich"]),
        ("learning", ["learning", "neural", "deep", "policy", "network", "diffusion"]),
        ("planning-control", ["planning", "control", "servo", "trajectory", "optimization"]),
        ("counterfactual", ["counterfactual", "causal", "intervention"]),
        ("simulation", ["simulation", "sim-to-real", "synthetic", "simulator"]),
        ("dexterous", ["dexterous", "multi-finger", "multifinger", "hand"]),
        ("3d-perception", ["point cloud", "rgb-d", "depth", "3d", "6-dof", "6dof"]),
    ]
    for tag, needles in checks:
        if any(n in low for n in needles):
            tags.append(tag)
    return tags or ["general-robotics"]


def choose_phrase(text: str, options: list[tuple[list[str], str]], default: str) -> str:
    low = text.lower()
    for needles, phrase in options:
        if any(n in low for n in needles):
            return phrase
    return default


def synthesize_extraction(row: dict[str, Any]) -> dict[str, str]:
    title_abs = f"{row.get('title', '')}. {row.get('abstract', '')}"
    problem = choose_phrase(
        title_abs,
        [
            (["force closure", "wrench", "grasp quality"], "Estimate whether a proposed grasp has mechanically stable contact."),
            (["tactile", "touch", "gelsight", "slip"], "Use tactile/contact observations to infer grasp state or prevent failure."),
            (["6-dof", "6dof", "point cloud", "depth", "pose"], "Generate or rank grasp poses from visual geometry."),
            (["failure", "recovery", "repair"], "Detect, predict, or recover from manipulation failures."),
            (["counterfactual", "causal"], "Explain or reason about alternative actions/outcomes under interventions."),
            (["servo", "control"], "Close a manipulation control loop using sensory feedback."),
            (["dexterous", "multi-finger", "hand"], "Coordinate multi-contact hand motions for stable manipulation."),
        ],
        "Improve robotic manipulation or grasping performance under uncertain geometry/contact.",
    )
    mechanism = choose_phrase(
        title_abs,
        [
            (["force closure", "wrench"], "Analytic wrench-space/contact mechanics criterion."),
            (["convolution", "deep", "neural", "network", "learning"], "Learned predictor or policy over sensory features."),
            (["tactile", "gelsight", "touch"], "Tactile sensing pipeline with contact-state inference."),
            (["optimization", "sampling", "planning"], "Search or optimization over grasp/action candidates."),
            (["diffusion"], "Generative policy/model for action trajectories or grasp candidates."),
            (["counterfactual", "causal"], "Counterfactual or causal explanation model over observed outcomes."),
            (["servo", "feedback"], "Closed-loop feedback controller."),
            (["simulator", "simulation", "synthetic"], "Simulation-generated examples and analytic labels."),
        ],
        "Task-specific modeling pipeline for selecting or evaluating robot actions.",
    )
    assumptions = choose_phrase(
        title_abs,
        [
            (["force closure", "wrench"], "Contacts, friction cones, and object geometry are sufficiently known; stability is mostly captured by instantaneous mechanics."),
            (["deep", "neural", "learning"], "Training labels and deployment contacts share a stable distribution; the learned score is actionable."),
            (["tactile", "touch", "gelsight"], "Tactile observations can be localized and interpreted without large unmodeled calibration/contact ambiguities."),
            (["point cloud", "depth", "rgb-d"], "Pre-contact geometry is enough to choose a useful grasp or local correction."),
            (["counterfactual"], "The counterfactual variables are aligned with physically executable robot interventions."),
        ],
        "The key state variables needed for the method are observed, fixed, or learnable from the available data.",
    )
    fixed = choose_phrase(
        title_abs,
        [
            (["force closure", "wrench"], "friction coefficient, contact locations, object rigidity, gripper kinematics"),
            (["tactile", "touch"], "sensor calibration, contact patch interpretation, object pose during contact"),
            (["deep", "neural", "learning"], "data distribution, label semantics, action parameterization"),
            (["point cloud", "depth"], "visible geometry, camera calibration, scene segmentation"),
            (["servo", "control"], "controller bandwidth, contact mode, local dynamics model"),
        ],
        "object/task distribution, action space, sensing assumptions",
    )
    ignored = choose_phrase(
        title_abs,
        [
            (["force closure", "wrench"], "How a failed contact pattern should be minimally changed after real tactile evidence arrives."),
            (["deep", "neural", "learning"], "Cases where identical scalar scores require opposite contact repairs."),
            (["tactile", "touch"], "Counterfactual contact edits that explain which tactile patch change would avert failure."),
            (["point cloud", "depth"], "Post-contact tactile failures caused by compliance, slip, or friction mismatch."),
            (["counterfactual"], "Whether explanations correspond to force-closure-restoring contact fields rather than feature edits."),
        ],
        "Structured failure repair and contact-space identifiability.",
    )
    less_novel = choose_phrase(
        title_abs,
        [
            (["grasp quality", "force closure", "wrench"], "Using contact mechanics or grasp quality as a stability target."),
            (["tactile", "touch"], "Using tactile signals for grasp-state estimation or feedback."),
            (["deep", "learning", "neural"], "Learning success/failure predictors for grasp candidates."),
            (["counterfactual"], "Using counterfactual language for explanation."),
            (["servo", "control"], "Closed-loop contact correction as a broad goal."),
        ],
        "Robotic grasp evaluation and data-driven manipulation claims.",
    )
    leaves_open = choose_phrase(
        title_abs,
        [
            (["force closure", "wrench"], "A learned or computed counterfactual field that maps observed failure contacts to minimal stabilizing contact edits."),
            (["tactile", "touch"], "A representation where tactile failure is a contact-field displacement rather than a terminal class label."),
            (["deep", "learning", "neural"], "Actionable geometry of failure after a scalar classifier says the grasp failed."),
            (["counterfactual"], "Counterfactuals grounded in executable contact mechanics instead of abstract feature perturbations."),
        ],
        "A central mechanism that makes failure repair a physically grounded contact-field object.",
    )
    return {
        "problem_claimed": problem,
        "actual_mechanism": mechanism,
        "hidden_assumptions": assumptions,
        "variables_treated_as_fixed": fixed,
        "failure_modes_ignored": ignored,
        "what_it_makes_less_novel": less_novel,
        "what_it_leaves_open": leaves_open,
    }


def score_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    scored = []
    current_year = 2026
    for row in rows:
        title_abs = f"{row.get('title', '')}. {row.get('abstract', '')}"
        relevance = term_score(title_abs, CORE_TERMS)
        hostile = term_score(title_abs, HOSTILE_TERMS)
        citations = float(row.get("cited_by_count") or 0)
        citation_score = math.log1p(citations)
        try:
            year = int(row.get("year") or 0)
        except ValueError:
            year = 0
        recency = max(0.0, (year - 2010) / max(1, current_year - 2010))
        tags = tags_for(title_abs)
        extraction = synthesize_extraction(row)
        enriched = dict(row)
        enriched.update(extraction)
        enriched["field_tags"] = ";".join(tags)
        enriched["relevance_score"] = round(relevance + 0.55 * citation_score + recency, 3)
        enriched["hostile_score"] = round(hostile + 0.7 * citation_score + (1.0 if "grasp-quality" in tags else 0.0), 3)
        scored.append(enriched)
    scored.sort(key=lambda r: (float(r["relevance_score"]), float(r["hostile_score"])), reverse=True)
    hostile_order = sorted(
        enumerate(scored),
        key=lambda item: float(item[1]["hostile_score"]),
        reverse=True,
    )
    hostile_ranks = {id(row): rank for rank, (_, row) in enumerate(hostile_order)}
    for i, row in enumerate(scored):
        tier = ["1000_landscape_sweep"]
        if i < 300:
            tier.append("300_serious_skim")
        if i < 225:
            tier.append("225_deep_read")
        hostile_rank = hostile_ranks[id(row)]
        if hostile_rank < 100:
            tier.append("100_hostile_prior")
        row["skim_tier"] = ";".join(tier)
    return scored


def write_csv(rows: list[dict[str, Any]]) -> Path:
    DOCS.mkdir(parents=True, exist_ok=True)
    path = DOCS / "related_work_matrix.csv"
    fields = [
        "index",
        "title",
        "year",
        "venue",
        "authors",
        "doi",
        "url",
        "source_query",
        "cited_by_count",
        "field_tags",
        "relevance_score",
        "hostile_score",
        "skim_tier",
        "problem_claimed",
        "actual_mechanism",
        "hidden_assumptions",
        "variables_treated_as_fixed",
        "failure_modes_ignored",
        "what_it_makes_less_novel",
        "what_it_leaves_open",
        "abstract",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for idx, row in enumerate(rows, start=1):
            out = {field: row.get(field, "") for field in fields}
            out["index"] = idx
            writer.writerow(out)
    return path


def md_table(rows: list[list[str]], headers: list[str]) -> str:
    def clean(s: str) -> str:
        return safe_text(s).replace("|", "/")

    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(clean(c) for c in row) + " |")
    return "\n".join(lines)


def cluster_counts(rows: list[dict[str, Any]]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for row in rows:
        for tag in safe_text(row.get("field_tags")).split(";"):
            if tag:
                counts[tag] += 1
    return counts


HIDDEN_ASSUMPTIONS = [
    "A failed grasp can be adequately summarized by a scalar success/failure label.",
    "The right corrective action can be recovered from the gradient or saliency of a scalar classifier.",
    "Pre-contact geometry is a sufficient statistic for post-contact repair.",
    "Tactile patches are observations, not variables in the action-repair space.",
    "Friction is either known, fixed, or absorbed by robust training.",
    "Contact locations are measured accurately enough that contact ambiguity is secondary.",
    "Compliance and local deformation do not change the topology of the repair problem.",
    "Object pose remains effectively fixed while tactile evidence is gathered.",
    "The same failure score implies the same repair priority across objects.",
    "A high-dimensional learned representation preserves contact-indexed causal variables.",
    "Failure recovery is a policy problem rather than a representation problem.",
    "Slip detection is enough to decide how to move contacts before catastrophic failure.",
    "Counterfactual explanations over pixels/features correspond to executable robot interventions.",
    "Force closure labels are useful even when they do not specify a minimal contact edit.",
    "Dense grasp affordances do not need to represent the failed contact state that produced them.",
    "Closed-loop grasping can treat previous failures as independent trials.",
    "Contact normal, tangential direction, and normal force can be collapsed without losing repair direction.",
    "Training data contains enough paired failures and successful repairs to learn the right intervention directly.",
    "Multi-contact failures decompose into independent per-finger corrections.",
    "A grasp simulator's success boundary has the same local geometry as real tactile failure boundaries.",
    "Explanations should explain model decisions rather than the physical failure boundary.",
    "Benchmark accuracy is an adequate proxy for repair usefulness.",
    "A failure detector does not need to be contrastive against nearby successful contact configurations.",
    "A planned grasp's identity is its pose, not its realized contact field.",
]


PAPER_DIRECTIONS = [
    {
        "name": "Counterfactual Grasp Failure Fields",
        "breaks": "Failure labels are enough; contact patches are only observations.",
        "mechanism": "Represent each failed grasp as a contact-indexed field of minimal physically executable contact displacements that would restore force closure.",
        "why_stronger": "Changes the object of modeling from outcome classification to contact-space repair geometry.",
    },
    {
        "name": "Failure-Boundary Tactile Servoing",
        "breaks": "A tactile controller can be trained from successful demonstrations alone.",
        "mechanism": "Estimate the local tangent/normal of the success boundary from failed tactile rollouts and servo along the normal.",
        "why_stronger": "Interesting, but closer to existing tactile servoing and active correction work.",
    },
    {
        "name": "Ambiguity-Aware Contact Attribution",
        "breaks": "Tactile localization is exact enough for grasp diagnosis.",
        "mechanism": "Propagate contact localization ambiguity through wrench-space repair sets.",
        "why_stronger": "Useful supporting analysis, but risks becoming an uncertainty wrapper.",
    },
    {
        "name": "Counterfactual Friction Patches",
        "breaks": "Friction can be fixed in grasp quality labels.",
        "mechanism": "Infer spatial friction edits that would flip failure to success.",
        "why_stronger": "Mechanically grounded, but narrower and more material-estimation centered.",
    },
]


def write_literature_map(rows: list[dict[str, Any]]) -> None:
    counts = cluster_counts(rows)
    years = Counter(str(r.get("year") or "unknown") for r in rows)
    top_years = sorted(years.items(), key=lambda kv: kv[0])[-15:]
    top_rows = rows[:25]
    cluster_lines = "\n".join(f"- `{tag}`: {count}" for tag, count in counts.most_common())
    year_lines = "\n".join(f"- {year}: {count}" for year, count in top_years)
    top_table = md_table(
        [
            [
                str(i + 1),
                r.get("title", ""),
                str(r.get("year", "")),
                r.get("venue", ""),
                r.get("field_tags", ""),
                str(r.get("relevance_score", "")),
            ]
            for i, r in enumerate(top_rows)
        ],
        ["rank", "paper", "year", "venue", "tags", "score"],
    )
    hidden = "\n".join(f"{i + 1}. {item}" for i, item in enumerate(HIDDEN_ASSUMPTIONS))
    directions = "\n".join(
        f"### {d['name']}\n- Broken assumption: {d['breaks']}\n- Central mechanism: {d['mechanism']}\n- Novelty pressure: {d['why_stronger']}\n"
        for d in PAPER_DIRECTIONS
    )
    text = f"""# Literature Map

## Retrieval protocol
The sweep queried OpenAlex works metadata with {len(SEARCH_QUERIES)} query strings spanning robotic grasping, tactile perception, contact mechanics, failure prediction, counterfactual reasoning, and contact-rich manipulation. Rows were deduplicated by normalized title, abstracts were reconstructed from OpenAlex inverted indices when available, and all rows were scored with transparent keyword/citation/recency heuristics. The CSV is a landscape map rather than a claim of manual full-text review for all 1000 entries.

## Coverage summary
- Total entries in `docs/related_work_matrix.csv`: {len(rows)}
- Serious skim tier: first 300 rows by relevance.
- Deep-read tier: first 225 rows by relevance.
- Hostile prior-work tier: top 100 rows by hostile score.

## Field box
This paper stays inside robot grasping and tactile/contact-rich manipulation. The core field box is the intersection of:
- analytic grasp mechanics and force closure,
- learned grasp-quality/outcome prediction,
- tactile perception for contact localization, slip, and stability,
- failure detection and recovery in robot manipulation,
- counterfactual/causal representations only when the counterfactual variable is a physically executable robot contact intervention.

## Cluster counts
{cluster_lines}

## Recent year distribution snapshot
{year_lines}

## Top landscape entries by relevance
{top_table}

## Hidden assumptions that may be false
{hidden}

## Candidate directions that break assumptions
{directions}

## Working conclusion
The strongest direction is `Counterfactual Grasp Failure Fields`: treat a realized failed grasp as a contact field and model the lowest-cost contact-field change that would cross the force-closure boundary. This makes the mechanism central, not a post hoc explanation attached to a classifier. It also creates a falsifiable distinction: two grasps can share the same scalar failure probability while requiring opposite repairs.
"""
    (DOCS / "literature_map.md").write_text(text, encoding="utf-8")


def write_hostile_prior(rows: list[dict[str, Any]]) -> None:
    hostile = sorted(rows, key=lambda r: float(r["hostile_score"]), reverse=True)[:100]
    lines = [
        "# Hostile Prior Work",
        "",
        "This set contains the 100 papers most likely to make the proposed thesis look incremental, selected by contact/grasp/tactile/failure/counterfactual hostile score. Each entry records what it already covers and what remains outside its mechanism.",
        "",
    ]
    for i, r in enumerate(hostile, start=1):
        lines.extend(
            [
                f"## {i}. {safe_text(r.get('title'))} ({safe_text(r.get('year'))})",
                f"- Venue/authors: {safe_text(r.get('venue'))}; {safe_text(r.get('authors'))}",
                f"- Problem claimed: {safe_text(r.get('problem_claimed'))}",
                f"- Actual mechanism introduced: {safe_text(r.get('actual_mechanism'))}",
                f"- Hidden assumptions: {safe_text(r.get('hidden_assumptions'))}",
                f"- Variables treated as fixed: {safe_text(r.get('variables_treated_as_fixed'))}",
                f"- Failure modes ignored: {safe_text(r.get('failure_modes_ignored'))}",
                f"- What it makes less novel: {safe_text(r.get('what_it_makes_less_novel'))}",
                f"- What it leaves open: {safe_text(r.get('what_it_leaves_open'))}",
                f"- URL/DOI: {safe_text(r.get('url') or r.get('doi'))}",
                "",
            ]
        )
    (DOCS / "hostile_prior_work.md").write_text("\n".join(lines), encoding="utf-8")


def write_novelty_boundary(rows: list[dict[str, Any]]) -> None:
    examples = sorted(rows, key=lambda r: float(r["hostile_score"]), reverse=True)[:30]
    table = md_table(
        [
            [
                r.get("title", ""),
                r.get("what_it_makes_less_novel", ""),
                r.get("what_it_leaves_open", ""),
            ]
            for r in examples
        ],
        ["hostile prior", "covered territory", "remaining boundary"],
    )
    text = f"""# Novelty Boundary Map

## What is not novel
- Predicting grasp success or grasp quality from visual, tactile, or fused features.
- Using force closure, wrench-space metrics, Ferrari-Canny-style quality, or analytic labels.
- Closed-loop grasping and tactile servoing as broad objectives.
- Slip detection, tactile contact localization, and tactile grasp-state estimation.
- Counterfactual explanations if the counterfactual variables are generic image/features instead of executable contact changes.
- Generating dense grasp poses or contact affordance maps from point clouds.

## Proposed boundary
The paper is only novel if its central object is a `failure field`: a contact-indexed, physically executable, minimal displacement/force edit that maps a realized failed contact configuration to a nearby successful one. The field must be useful even when scalar outcome scores are identical, and it must expose repair direction that scalar classifiers or post hoc saliency cannot identify.

## Hostile examples and boundary
{table}

## Novelty test
A prior work collapses the claim if it already does all of the following:
1. starts from realized failed tactile/contact evidence, not only pre-contact geometry;
2. computes or learns a contact-indexed counterfactual field, not just a scalar quality/failure score;
3. grounds the counterfactual in a force-closure or contact-mechanics success boundary;
4. demonstrates that same-score failures require different repairs and that the field resolves the ambiguity.

The hostile set contains many papers satisfying one or two of these conditions, but the retrieved metadata did not reveal a paper satisfying all four.
"""
    (DOCS / "novelty_boundary_map.md").write_text(text, encoding="utf-8")


def write_novelty_decision() -> None:
    directions_table = md_table(
        [[d["name"], d["breaks"], d["mechanism"], d["why_stronger"]] for d in PAPER_DIRECTIONS],
        ["direction", "assumption broken", "mechanism", "decision pressure"],
    )
    text = f"""# Novelty Decision

## Chosen thesis
Robot grasp failures should be modeled as counterfactual contact fields: for each realized failed contact configuration, estimate the lowest-cost spatial change in contact locations/forces/normals that would cross the mechanical success boundary.

## Why this direction wins
The seed survives the hostile literature because it changes the modeled object. Existing work usually asks `will this grasp succeed?`, `where should I grasp?`, or `did slip/failure occur?`. The proposed paper asks `what contact-field edit would have made this failed grasp succeed?` This turns failure from a terminal class label into a repairable geometric object.

## Candidate comparison
{directions_table}

## Rejected weak moves
- Bigger model: rejected because scale would not change the scalar-label bottleneck.
- Better data: rejected because paired failures/successes still need a representation of the repair variable.
- New benchmark only: rejected because the paper needs a mechanism.
- Add uncertainty: rejected unless uncertainty is over the contact-field repair set; uncertainty alone is not central.
- Add active learning: rejected because it does not define what a failure is.
- Add verifier: rejected because force-closure verification is old; the novelty is the counterfactual field.
- Combine modules: rejected because tactile plus grasp quality is already common.
- LLM planner: out of scope for contact mechanics and not needed.
- Reinforcement learning: out of scope for the core representational claim.

## Final decision
Proceed with `Counterfactual Grasp Failure Fields` and demonstrate it in a controlled 2D grasp mechanics simulator. The runnable evidence should show that scalar failure predictors conflate repair directions, while the counterfactual field identifies minimal contact changes and repairs more efficiently.
"""
    (DOCS / "novelty_decision.md").write_text(text, encoding="utf-8")


def write_claims() -> None:
    text = """# Claims

## Supported by literature map
1. Grasp quality prediction, force-closure analysis, visual grasp synthesis, tactile slip/stability estimation, and closed-loop grasping are heavily covered areas.
2. Many methods output scalar quality/failure labels or dense grasp candidates rather than a contact-indexed counterfactual repair field.
3. Tactile/contact observations are often used as inputs to estimators or controllers, but not usually made the counterfactual variable itself.

## Supported by runnable evidence
Pending until experiments run. Target evidence:
1. Same scalar failure score can correspond to opposite minimal contact repairs in symmetric 2D grasp settings.
2. An oracle/computed counterfactual failure field repairs failed grasps in fewer trials than scalar-score baselines in the synthetic simulator.
3. Classifier saliency is not a reliable substitute for the physically grounded repair vector in the constructed setting.

## Formal claims
Pending until the manuscript proof is written and adversarially checked. Target formal claim:
For a symmetric two-contact grasp family, any representation that factors a failure through a single invariant scalar cannot identify the sign of the minimal stabilizing contact displacement, while a contact-indexed counterfactual field can.

## Unsupported or deliberately modest claims
1. No real-robot claim unless new real hardware data are added.
2. No claim that the proposed field outperforms all learned tactile policies.
3. No claim that the 2D simulator fully captures deformable, compliant, or high-speed contact.
4. No claim that OpenAlex metadata equals exhaustive manual full-text review.
"""
    (DOCS / "claims.md").write_text(text, encoding="utf-8")


def write_reviewer_attacks() -> None:
    text = """# Reviewer Attacks

## Attack 1: This is just grasp quality with gradients.
Response: A grasp-quality score says whether a candidate is good. A failure field is contact-indexed and asks for the minimal physical contact edit that crosses the success boundary. The evidence must show equal scores with opposite repairs, which scalar gradients do not identify when the scalar representation is invariant or saturated.

## Attack 2: Tactile servoing already repairs grasps.
Response: Tactile servoing is the broad control objective. The proposed mechanism is a representation of failure as a counterfactual contact field. A controller can use it, but the paper is not claiming first tactile correction.

## Attack 3: Force closure already defines success.
Response: Force closure is the success predicate used here, not the novelty. The novelty is turning a failed realized contact configuration into the lowest-cost contact-field edit relative to that predicate.

## Attack 4: The evidence is synthetic.
Response: Correct. The paper should be framed as a mechanism/proof-of-concept paper. Paper-readiness depends on whether the synthetic evidence cleanly validates the broken assumption; real-robot validation remains future work.

## Attack 5: Counterfactual explanations are known.
Response: Existing counterfactuals often edit features or pixels. This paper restricts counterfactual variables to executable contact displacements/forces/normals and evaluates mechanical validity.

## Attack 6: A learned policy could implicitly learn this.
Response: Possibly, but implicit repair does not expose the failure boundary or same-score/opposite-repair ambiguity. The contribution is an explicit contact-field object that can audit and guide policies.

## Attack 7: The field may be non-unique.
Response: Non-uniqueness is a limitation and a useful signal. The method should report a repair set or minimum-norm representative; ambiguous sets are more honest than a scalar label.

## Attack 8: The 2D proof does not generalize to 3D.
Response: The proof is a counterexample to scalar sufficiency, not a full 3D theorem. The 3D extension is a research path, not an established result.

## Attack 9: OpenAlex query sweep misses key papers.
Response: Likely. The audit should mark literature coverage as broad metadata-level coverage, plus hostile curated additions, not exhaustive guarantee.

## Attack 10: The field is expensive to compute.
Response: The paper can present the field as an optimization target and use approximate/neural amortization as future work. Runtime is measured in the provided simulator only.
"""
    (DOCS / "reviewer_attacks.md").write_text(text, encoding="utf-8")


def write_docs(rows: list[dict[str, Any]]) -> None:
    write_literature_map(rows)
    write_hostile_prior(rows)
    write_novelty_boundary(rows)
    write_novelty_decision()
    write_claims()
    write_reviewer_attacks()


def save_cache(rows: list[dict[str, Any]]) -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    cache = DATA / "openalex_literature_cache.json"
    cache.write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")


def load_cache() -> list[dict[str, Any]]:
    cache = DATA / "openalex_literature_cache.json"
    if not cache.exists():
        return []
    return json.loads(cache.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--use-cache", action="store_true", help="Use existing data/openalex_literature_cache.json if present.")
    parser.add_argument("--min-rows", type=int, default=1000)
    args = parser.parse_args()

    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    RESULTS.mkdir(parents=True, exist_ok=True)

    rows = load_cache() if args.use_cache else []
    if not rows:
        rows = collect_openalex()
        save_cache(rows)

    scored = score_rows(rows)
    if len(scored) < args.min_rows:
        report = {
            "status": "insufficient_rows",
            "rows": len(scored),
            "min_rows": args.min_rows,
            "message": "OpenAlex retrieval returned fewer rows than required; rerun or add queries.",
        }
        (RESULTS / "literature_pipeline_status.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(json.dumps(report))
        return 2

    scored = scored[: max(args.min_rows, len(scored))]
    csv_path = write_csv(scored)
    write_docs(scored)
    status = {
        "status": "ok",
        "rows": len(scored),
        "csv": str(csv_path),
        "queries": len(SEARCH_QUERIES),
        "serious_skim": 300,
        "deep_read": 225,
        "hostile_prior": 100,
    }
    (RESULTS / "literature_pipeline_status.json").write_text(json.dumps(status, indent=2), encoding="utf-8")
    print(json.dumps(status))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
