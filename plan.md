# Plan

## Mission

Build an honest, runnable robotics paper around paper 02, starting from the seed "Counterfactual Grasp Failure Fields" but allowing the thesis to change if the literature makes a stronger direction obvious.

## Non-interactive safety

- Use short, guarded PowerShell commands with explicit existence checks or `try/catch`.
- Avoid bare probes that may exit nonzero.
- Avoid Unix here-doc syntax.
- Keep long work chunked and resumable, with artifacts written under `docs/`, `data/`, `scripts/`, `results/`, and `paper/`.
- Reuse any existing retry artifacts after inspection.

## Stages

1. Initialize status and inspect repository state, tools, caches, and prior artifacts.
2. Build or resume a broad robotics grasping/tactile/failure literature corpus with at least 1000 rows in `docs/related_work_matrix.csv`.
3. Produce a 300-paper serious skim, a 200-250-paper deep read, and a 100-paper hostile prior-work set.
4. Extract assumptions, mechanisms, fixed variables, ignored failures, novelty erosion, and open space for important papers.
5. Define the field box, enumerate at least 20 false hidden assumptions, generate candidate paper directions, and choose the strongest thesis.
6. Implement runnable evidence that tests whether the broken assumption matters.
7. Write required audit documents:
   - `docs/literature_map.md`
   - `docs/hostile_prior_work.md`
   - `docs/novelty_boundary_map.md`
   - `docs/novelty_decision.md`
   - `docs/claims.md`
   - `docs/reviewer_attacks.md`
   - `docs/final_audit.md`
8. Fetch the latest official ICLR LaTeX template available at runtime, write an anonymous ICLR-style paper, and compile the PDF.
9. Save the final PDF exactly to `C:/Users/wangz/Downloads/02.pdf`.
10. Create or reuse the public GitHub repository `02_counterfactual_grasp_failure_fields`, push the complete repo, and document the URL or failure.
11. Final verification: runnable repo, compiled or documented paper status, honest claims, final audit, exact PDF path, GitHub push status, and desktop-copy status.

## Paper quality constraints

- Do not rely on weak moves such as bigger models, more data, uncertainty, active learning, verifier boltons, LLM planning, or reinforcement learning unless a genuinely new mechanism is justified.
- Make the central mechanism change explicit.
- Demonstrate or prove that the broken assumption matters.
- Mark unsupported claims honestly.
- Prefer compact but reproducible experiments over overclaimed empirical breadth.
