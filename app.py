import streamlit as st
import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🤖 AI Data Analyst Agent")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    question = st.text_input("Ask a question about the data")

    if st.button("Analyze"):
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

        st.subheader("AI Answer")
        st.write(response.text)