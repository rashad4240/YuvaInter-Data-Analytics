# Task 4 – Data Science Tool Mastery Project

**YuvaIntern · Data Analyst Internship** · **Intern:** Rashad Kazi

Eight industry-standard tools applied to one real dataset, with a portfolio piece for each.

## Dataset
Diabetes dataset – Efron, Hastie, Johnstone & Tibshirani (2004), *Least Angle Regression*. 442 patients, 10 baseline measurements (age, sex, BMI, blood pressure, six blood serum values) and disease progression after one year. Unscaled values (`load_diabetes(scaled=False)`).

## Portfolio pieces
| File | What it shows |
|---|---|
| `task4_tool_mastery.ipynb` | All exercises with outputs |
| `eda_toolkit.py` | Reusable module: `quick_profile()`, `build_excel_report()` |
| `sql/diabetes_queries.sql` | GROUP BY, CASE/HAVING, window `RANK()`, sub-queries |
| `output/diabetes.db` | SQLite database built from the data |
| `output/Diabetes_Analysis_Report.xlsx` | Automated Excel report: live formulas, conditional formatting, native chart |
| `output/model_comparison.csv` | scikit-learn model results |
| `figures/` | Chart gallery, heatmap, feature effects, actual vs predicted, Excel screenshot |
| `Task4_Data_Science_Tool_Mastery_Report.docx` / `.pdf` | Written report |

## Tools and results
| Tool | Result |
|---|---|
| NumPy | Vectorised z-scores ~300× faster than a loop; broadcasting over a 442×9 matrix |
| Pandas | Five features in one method chain (BMI class, age group, BP flag, quartile, group-relative BMI) |
| SQL | Four queries; Q1 matches Pandas exactly |
| Seaborn | Four-panel gallery and masked heatmap |
| SciPy | BMI r = 0.59, glucose ρ = 0.35, BP χ² = 70.4, BMI-class F = 57.4 (all p < 0.001); sex not significant (p = 0.37) |
| scikit-learn | Ridge best CV R² = 0.48 (test R² 0.46, MAE 42.9); top drivers BMI, log-triglycerides, BP |
| openpyxl | Four-sheet workbook, 20 formulas, 0 errors |

## Run
```bash
pip install -r requirements.txt
jupyter notebook task4_tool_mastery.ipynb
```
