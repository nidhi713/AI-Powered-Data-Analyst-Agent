import pandas as pd
import matplotlib.pyplot as plt

def create_chart(file_path):
    df = pd.read_csv(file_path)

    dept_salary = df.groupby("Department")["Salary"].mean()

    dept_salary.plot(kind="bar")

    plt.title("Average Salary by Department")
    plt.ylabel("Salary")

    plt.savefig("salary_chart.png")