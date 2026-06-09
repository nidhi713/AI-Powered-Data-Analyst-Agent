import os
from dotenv import load_dotenv
import google.generativeai as genai
import pandas as pd
from charts import create_chart

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

csv_file = input("Enter CSV file name: ")

df = pd.read_csv(csv_file)
summary = df.to_string()

create_chart(csv_file)

question = input("Ask a question about the data: ")

prompt = f"""
You are a data analyst.

Dataset:
{df.to_string()}

Rules:
1. Calculate values directly from the dataset.
2. Show calculations when needed.
3. Do not guess.
4. If there is a tie, mention it.

Question:
{question}
"""

response = model.generate_content(prompt)

print("\nAI Answer:\n")
print(response.text)