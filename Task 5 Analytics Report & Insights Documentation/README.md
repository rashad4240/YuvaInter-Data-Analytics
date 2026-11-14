# Task 5 – Analytics Report & Insights: US Technology Stocks vs the Market

**YuvaIntern · Data Analyst Internship** · **Intern:** [Your Name]

A stakeholder-ready analytics report for a (case-study) investment committee reviewing its technology allocation.

## Business questions
1. Which stocks created the most value, and did they beat the S&P 500 and NASDAQ?
2. How much risk came with that return?
3. How did the stocks behave in the dot-com crash, the 2008 crisis, COVID-19 and the 2022 sell-off?
4. Does holding several of them reduce risk?

## Data
Monthly adjusted closing prices from Yahoo Finance (`data/Stocks.csv`, from Matplotlib's sample data): IBM, Apple, Microsoft, Xerox, Amazon, Dell, Alphabet, Adobe, S&P 500, NASDAQ – Jan 1990 to Jun 2022.

**Cleaning:** removed comment line, 133 empty rows and one duplicated end-of-June row; kept pre-listing gaps as true missing values; compared stocks on a common window (Sep 2004 – Jun 2022).

## Files
| File / folder | Description |
|---|---|
| `task5_stock_performance_analytics.ipynb` | Analysis notebook |
| `Task5_Analytics_Report_and_Insights.docx` / `.pdf` | Report with executive summary and recommendations |
| `output/` | Clean prices, monthly returns, KPI tables (CSV) |
| `figures/` | Six charts |

## Headline results (Sep 2004 – Jun 2022)
| | Value of 1 | CAGR | Volatility | Return/risk | Max drawdown |
|---|---|---|---|---|---|
| Apple | 232.3 | 35.9% | 33.1% | 1.09 | -57% |
| Amazon | 52.6 | 25.0% | 36.3% | 0.69 | -54% |
| Alphabet | 34.5 | 22.1% | 30.1% | 0.73 | -59% |
| Microsoft | 14.6 | 16.3% | 22.8% | 0.72 | -55% |
| S&P 500 | 3.4 | 7.2% | 14.7% | 0.49 | -53% |
| Equal-weight 7 stocks | – | 19.3% | 20.4% | 0.94 | -49% |

- 5 of 7 stocks beat the S&P 500; IBM lagged and Xerox lost money
- Average correlation between stocks 0.39 → diversification cut risk by 31%

## Recommendations
Diversified technology basket · size positions by drawdown tolerance · yearly benchmark review · broad-market core alongside a technology sleeve.

*Educational analysis of historical data, not investment advice.*
