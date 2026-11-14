"""eda_toolkit – small, reusable helpers for exploratory analysis and reporting.

Author: Rashad kazi – YuvaIntern Data Analyst Internship, Task 4
"""
import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

HEADER_FILL = PatternFill("solid", start_color="1F4E79")
HEADER_FONT = Font(name="Arial", bold=True, color="FFFFFF")
BODY_FONT = Font(name="Arial", size=10)
INPUT_FONT = Font(name="Arial", size=10, color="0000FF")   # hard-coded inputs in blue
THIN = Side(style="thin", color="BFCFE0")
BORDER = Border(top=THIN, bottom=THIN, left=THIN, right=THIN)


def quick_profile(df: pd.DataFrame) -> pd.DataFrame:
    """Print shape, missing values and duplicates, and return a per-column profile."""
    print(f"Rows: {len(df):,} | Columns: {df.shape[1]} | "
          f"Missing cells: {int(df.isna().sum().sum())} | Duplicate rows: {int(df.duplicated().sum())}")
    profile = pd.DataFrame({
        "dtype": df.dtypes.astype(str),
        "missing": df.isna().sum(),
        "unique": df.nunique(),
        "min": df.min(numeric_only=True),
        "mean": df.mean(numeric_only=True).round(2),
        "max": df.max(numeric_only=True),
    })
    print(profile.to_string())
    return profile


def _write_table(ws, frame: pd.DataFrame, start_row: int = 1, start_col: int = 1, input_cols=()):
    for j, col in enumerate(frame.columns):
        c = ws.cell(row=start_row, column=start_col + j, value=str(col))
        c.fill, c.font, c.border = HEADER_FILL, HEADER_FONT, BORDER
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    for i, row in enumerate(frame.itertuples(index=False), start=1):
        for j, value in enumerate(row):
            if hasattr(value, "item"):
                value = value.item()
            c = ws.cell(row=start_row + i, column=start_col + j, value=value)
            c.font = INPUT_FONT if frame.columns[j] in input_cols else BODY_FONT
            c.border = BORDER
            if isinstance(value, float):
                c.number_format = "0.000"
    for j, col in enumerate(frame.columns):
        width = max(len(str(col)), *(len(f"{v}") for v in frame.iloc[:, j].head(200))) + 2
        ws.column_dimensions[get_column_letter(start_col + j)].width = min(max(width, 10), 40)
    ws.freeze_panes = ws.cell(row=start_row + 1, column=start_col)


def build_excel_report(features: pd.DataFrame, scores: pd.DataFrame, tests: pd.DataFrame, path: str) -> str:
    """Create a formatted Excel workbook: Summary (live formulas + chart), Data, Models, Tests."""
    wb = Workbook()

    # --- Data sheet (raw values; formulas on Summary point here)
    data = features[["age", "sex", "bmi", "bp", "glucose", "progression", "bmi_class", "age_group"]].copy()
    data[["bmi_class", "age_group"]] = data[["bmi_class", "age_group"]].astype(str)
    ws_data = wb.active
    ws_data.title = "Data"
    _write_table(ws_data, data, input_cols=set(data.columns))
    n = len(data) + 1  # last data row

    # --- Summary sheet with live formulas
    ws = wb.create_sheet("Summary", 0)
    ws["A1"] = "Diabetes Progression – Automated Summary"
    ws["A1"].font = Font(name="Arial", bold=True, size=14, color="1F4E79")
    ws["A2"] = "All figures below are live Excel formulas that read the Data sheet."
    ws["A2"].font = Font(name="Arial", italic=True, size=9, color="5A5A5A")
    headers = ["BMI class", "Patients", "Avg progression", "Avg BMI", "Share of patients"]
    for j, h in enumerate(headers, start=1):
        c = ws.cell(row=3, column=j, value=h)
        c.fill, c.font, c.border = HEADER_FILL, HEADER_FONT, BORDER
        c.alignment = Alignment(horizontal="center", wrap_text=True)
    classes = [c for c in ["Underweight", "Normal", "Overweight", "Obese"] if c in set(data.bmi_class)]
    for i, cls in enumerate(classes, start=4):
        ws.cell(row=i, column=1, value=cls)
        ws.cell(row=i, column=2, value=f'=COUNTIF(Data!$G$2:$G${n},A{i})')
        ws.cell(row=i, column=3, value=f'=AVERAGEIF(Data!$G$2:$G${n},A{i},Data!$F$2:$F${n})').number_format = "0.0"
        ws.cell(row=i, column=4, value=f'=AVERAGEIF(Data!$G$2:$G${n},A{i},Data!$C$2:$C${n})').number_format = "0.0"
        ws.cell(row=i, column=5, value=f'=B{i}/$B${4 + len(classes)}').number_format = "0.0%"
        for j in range(1, 6):
            ws.cell(row=i, column=j).font, ws.cell(row=i, column=j).border = BODY_FONT, BORDER
    t = 4 + len(classes)
    ws.cell(row=t, column=1, value="Total").font = Font(name="Arial", bold=True)
    ws.cell(row=t, column=2, value=f"=SUM(B4:B{t-1})").font = Font(name="Arial", bold=True)
    ws.cell(row=t, column=3, value=f"=AVERAGE(Data!$F$2:$F${n})").number_format = "0.0"
    ws.cell(row=t, column=4, value=f"=AVERAGE(Data!$C$2:$C${n})").number_format = "0.0"
    ws.cell(row=t, column=5, value=f"=SUM(E4:E{t-1})").number_format = "0.0%"
    for j in range(1, 6):
        ws.cell(row=t, column=j).border = BORDER
    ws.conditional_formatting.add(f"C4:C{t-1}", ColorScaleRule(start_type="min", start_color="EAF1F8",
                                                               end_type="max", end_color="2A78D6"))
    for col, w in zip("ABCDE", [16, 11, 16, 11, 16]):
        ws.column_dimensions[col].width = w

    chart = BarChart()
    chart.title = "Average progression by BMI class"
    chart.y_axis.title = "Progression score"
    chart.add_data(Reference(ws, min_col=3, min_row=3, max_row=t - 1), titles_from_data=True)
    chart.set_categories(Reference(ws, min_col=1, min_row=4, max_row=t - 1))
    chart.legend = None
    chart.height, chart.width = 7.5, 14
    ws.add_chart(chart, "G3")

    # --- Model and test sheets
    _write_table(wb.create_sheet("Models"), scores.round(3))
    tests_out = tests.copy()
    tests_out["Significant (5%)"] = tests_out["Significant (5%)"].map({True: "Yes", False: "No"})
    _write_table(wb.create_sheet("Statistical tests"), tests_out.round(4))

    wb.save(path)
    return path
