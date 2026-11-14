# Task 3 – Real-World Dataset Analysis: 145 Years of Global Temperature

**YuvaIntern · Data Analyst Internship** · **Intern:** [Your Name]

## Dataset
**NASA GISS Surface Temperature Analysis (GISTEMP v4)** – Land-Ocean Temperature Index, Global Means (`data/GLB.Ts+dSST.csv`).
Monthly global temperature anomalies in °C relative to the 1951–1980 average, 1880 onwards.

## Questions
1. How much has the planet warmed since 1880?
2. Is the warming accelerating?
3. Which years, decades, months and seasons are warmest?
4. Is recent warming beyond natural year-to-year variation?

## Files
| File / folder | Description |
|---|---|
| `task3_global_temperature_analysis.ipynb` | Full analysis notebook |
| `Task3_Real_World_Dataset_Analysis_Report.docx` / `.pdf` | Written report |
| `data/GLB.Ts+dSST.csv` | Raw NASA file |
| `data/gistemp_*.csv` | Cleaned wide, annual and long monthly tables |
| `figures/` | Six charts |

## Data cleaning
| Problem | Fix |
|---|---|
| Title line above header | `skiprows=1` |
| `***` placeholders (17 cells) | replaced with `NaN` |
| 16 numeric columns read as text | `pd.to_numeric` |
| Partial year 2026 | excluded from annual stats |
| Wide monthly layout | `melt` to long format with dates (1,754 rows) |
| Outliers | z-score vs 30-year rolling trend; real El Niño events kept |

## Key findings
- **+1.27 °C** warming from the 1880–1909 average to the last 10 years
- Trend: +0.02 °C/decade (1880–1940) → **+0.21** (1981–2025) → **+0.26** (2001–2025)
- All 10 warmest years are from 2015 onwards; 2024 is the warmest (+1.28 °C); warmest month September 2023 (+1.48 °C)
- Every month warmed by 0.9–1.1 °C
- 1996–2025 is 6.8 standard deviations warmer than 1951–1980 (Welch t = 15.1, p < 0.001)

## Run
```bash
pip install -r requirements.txt
jupyter notebook task3_global_temperature_analysis.ipynb
```

Source: GISTEMP Team, NASA Goddard Institute for Space Studies.
