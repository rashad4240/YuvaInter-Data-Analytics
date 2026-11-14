# Task 6 – Final Capstone: Predicting Breast Cancer Malignancy

**YuvaIntern · Data Analyst Internship** · **Intern:** Rashad kazi

## Problem
Build an explainable machine-learning screening aid that predicts whether a breast mass is **malignant** or **benign** from 30 cell-nucleus measurements taken from a fine needle aspirate, putting the detection of cancers first.

**Success criteria (set before modelling):** recall ≥ 0.97 · precision ≥ 0.90 · ROC-AUC ≥ 0.98

## Data
Breast Cancer Wisconsin (Diagnostic) – Wolberg, Street & Mangasarian, University of Wisconsin; UCI Machine Learning Repository. 569 patients (212 malignant, 357 benign), 30 features. Copy in `data/`.

## Method
1. EDA – Mann-Whitney tests with Bonferroni correction, effect sizes, correlation (multicollinearity)
2. Feature engineering – worst-to-mean ratios, shape irregularity, log transforms (tested honestly: tiny gain)
3. Six models with 5-fold stratified CV – baseline, logistic regression, KNN, SVM, random forest, gradient boosting
4. GridSearchCV tuning of the top two
5. Safety-first decision threshold chosen from out-of-fold predictions (0.25)
6. One final evaluation on the untouched test set
7. Explanation (coefficients, permutation importance), error analysis, learning curve

## Results (114 unseen test patients)
| Metric | Target | Result |
|---|---|---|
| Recall | ≥ 0.97 | **0.976** (41/42 cancers found) |
| Precision | ≥ 0.90 | **0.976** |
| ROC-AUC | ≥ 0.98 | **0.997** |
| Accuracy | – | 0.982 |

Selected model: tuned logistic regression (C = 1), threshold 0.25. Top drivers: worst texture, symmetry, concavity and concave points.

## Files
| File / folder | Description |
|---|---|
| `task6_capstone_breast_cancer_classification.ipynb` | Full notebook |
| `Task6_Capstone_Project_Report.docx` / `.pdf` | Project report |
| `Task6_Capstone_Presentation.pptx` | 11-slide presentation with speaker notes |
| `output/` | CV comparison and test results (CSV) |
| `figures/` | Six charts |

## Limitations
Single-hospital data from the early 1990s; small test set; no clinical history; research prototype only – not a medical device.

## Run
```bash
pip install -r requirements.txt
jupyter notebook task6_capstone_breast_cancer_classification.ipynb
```
