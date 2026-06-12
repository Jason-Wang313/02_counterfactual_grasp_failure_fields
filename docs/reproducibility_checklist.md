# Reproducibility Checklist

## Environment

- Python dependency: `matplotlib>=3.5`.
- Standard library only for mechanics/sampling.
- LaTeX build: `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` from `paper/`.

## Commands

```powershell
python -m pip install -r requirements.txt
python experiments/run_counterfactual_fields.py --n 20000 --seed 2
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
- `paper/main.pdf`
- `C:/Users/wangz/Downloads/02.pdf`

## Known Non-Reproducible Pieces

- Literature sweep depends on external API state if rerun.
- No hardware data exists.
- No pinned lockfile exists.
