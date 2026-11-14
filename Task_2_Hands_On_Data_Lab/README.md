# Task 2 – Hands-On Data Lab Implementation

**YuvaIntern · Data Analyst Internship** · **Intern:** Rashad Kazi
## Objective
1. Set up a data science environment with Python, Jupyter and the required libraries.
2. Complete practical exercises in data manipulation, visualisation and basic analysis.

## Dataset
Wine recognition dataset – UCI Machine Learning Repository. 178 wines from three cultivars, 13 chemical measurements (loaded with `sklearn.datasets.load_wine`, copy saved in `data/wine.csv`).

## Files
| File / folder | Description |
|---|---|
| `task2_hands_on_data_lab.ipynb` | Notebook with setup check, exercises, charts and analysis |
| `Task2_Hands_On_Data_Lab_Report.docx` / `.pdf` | Written report |
| `data/` | `wine.csv` (raw) and `wine_enriched.csv` (with new features) |
| `figures/` | Six charts |
| `requirements.txt` | Libraries needed to rebuild the lab |

## Environment setup
```bash
python -m venv dslab
dslab\Scripts\activate            # Windows  (macOS/Linux: source dslab/bin/activate)
pip install -r requirements.txt
jupyter notebook
```

## Exercises
- **Manipulation:** filtering, sorting and ranking, new columns with `pd.cut`, `groupby().agg()`, `crosstab` and `pivot_table`, `merge`, `melt`, `apply`, group-wise median imputation
- **Visualisation:** bar chart, histogram, box plot, scatter plot, correlation heatmap, violin plot
- **Analysis:** one-way ANOVA for all 13 features, Pearson correlation and linear regression

## Key findings
- Cultivar A: strong wines (13.7% alcohol) with very high proline (1,116 mg/L)
- Cultivar B: light wines with low colour intensity (3.1)
- Cultivar C: deep colour (7.4) but very low flavanoids (0.78)
- Best separators: flavanoids (F = 234), proline (F = 208), OD280/OD315 (F = 190); all 13 features significant (p < 0.001)
- Alcohol vs colour intensity: r = 0.55, R² = 0.30
