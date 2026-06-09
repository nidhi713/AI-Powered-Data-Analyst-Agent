import pandas as pd

def analyze_data(file_path):
    df = pd.read_csv(file_path)

    dept_avg_salary = df.groupby("Department")["Salary"].mean()

    summary = f"""
Rows: {df.shape[0]}
Columns: {df.shape[1]}

Columns:
{list(df.columns)}

Department Average Salaries:
{dept_avg_salary}

Statistics:
{df.describe()}
"""

    return summary