# Task 1 – Data Science Fundamentals Assessment

**YuvaIntern · Data Analyst Internship** (18 Sep 2026 – 13 Nov 2026)
**Intern:** Rashad kazi 

## Objective
Demonstrate understanding of core data science concepts – Python basics, statistical foundations, data types and industry best practices – and complete assignments covering all of these fundamentals.

## Files
| File | Description |
|---|---|
| `task1_data_science_fundamentals.ipynb` | Jupyter Notebook with all code, outputs and charts |
| `Task1_Data_Science_Fundamentals_Report.docx` | Full written report (Word) |
| `Task1_Data_Science_Fundamentals_Report.pdf` | Same report as PDF |
| `figures/` | Charts produced by the notebook |

## What the notebook covers
1. **Python basics** – built-in types, control flow, functions, error handling, list comprehensions
2. **Data types** – NumPy arrays vs lists, Pandas dtypes, nominal / ordinal / discrete / continuous data
3. **Statistical foundations** (Iris dataset) – descriptive statistics, correlation, Central Limit Theorem simulation, 95% confidence intervals, Welch's t-test
4. **Industry best practices** – reproducibility, CRISP-DM, data quality, PEP 8, version control, ethics
5. **Assignment** – 10 questions answered with code (IQR outliers, z-scores, groupby, Shapiro–Wilk, probability simulation, etc.)

## Key results
- Petal length is bimodal: mean 3.76 cm is below the median 4.35 cm because *setosa* forms its own cluster.
- Petal length and petal width are very strongly correlated (r = 0.96).
- Sample means of a skewed population were bell-shaped, confirming the Central Limit Theorem.
- *Virginica* has a significantly longer sepal than *versicolor* (Welch t = -5.63, p = 1.9 × 10⁻⁷).

## How to run
```bash
pip install -r requirements.txt
jupyter notebook task1_data_science_fundamentals.ipynb
```

## Tools
Python 3 · Jupyter · NumPy · Pandas · SciPy · Matplotlib · scikit-learn

## Dataset
Iris flower dataset – R. A. Fisher (1936), UCI Machine Learning Repository (loaded with `sklearn.datasets.load_iris`).
