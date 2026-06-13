# Reproducibility Checklist

## Environment

- Python dependency: `matplotlib>=3.5`.
- Standard library only for mechanics/sampling.
- LaTeX build: `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` from `paper/`.

## Commands

```powershell
python -m pip install -r requirements.txt
python experiments/run_counterfactual_fields.py --n 20000 --seed 2
python experiments/run_full_scale_fields.py
python experiments/run_full_scale_fields.py --summarize-only
cd paper
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Expected Outputs

- `results/counterfactual_field_cases.csv`
- `results/counterfactual_field_summary.json`
- `results/same_score_pairs.csv`
- `results/seed_stress_summary.csv`
- `results/stress_summary.json`
- `results/same_score_opposite_repairs.png`
- `results/repair_success_rates.png`
- `results/pair_failure_fields.png`
- `results/stress_success_rates.png`
- `results/full_scale/linear_contact_grid.csv`
- `results/full_scale/biased_scalar_grid.csv`
- `results/full_scale/mask_limit_grid.csv`
- `results/full_scale/noise_mismatch_grid.csv`
- `results/full_scale/large_seed_stress.csv`
- `results/full_scale/leaderboard.csv`
- `results/full_scale/full_scale_summary.json`
- `paper/figures/full_scale_success_leaderboard.png`
- `paper/figures/bias_worst_group_curve.png`
- `paper/figures/mask_limit_feasibility_map.png`
- `paper/figures/noise_mismatch_success.png`
- `paper/tables/full_scale_leaderboard.tex`
- `paper/tables/bias_worst_group_table.tex`
- `paper/tables/mask_feasibility_table.tex`
- `paper/tables/noise_boundary_table.tex`
- `paper/main.pdf` as the transient local build artifact before final copy/removal.
- `C:/Users/wangz/Downloads/02.pdf`

## Known Non-Reproducible Pieces

- Literature sweep depends on external API state if rerun.
- No hardware data exists.
- No pinned lockfile exists.

## Final Gate

- Full-scale runner writes 253,080 streamed baseline rows and stores no raw trajectories.
- Final local build verified at 26 pages before copying to Downloads.
- Downloads copy allowed only after the PDF text is verified as the actual paper.
- After copying, remove the transient local `paper/main.pdf`; the canonical final PDF is `C:/Users/wangz/Downloads/02.pdf`.
