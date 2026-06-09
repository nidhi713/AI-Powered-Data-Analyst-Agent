from typing import TypedDict
import pandas as pd
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

class AgentState(TypedDict):
    csv_file: str
    summary: str
    insights: str
    question: str
    answer: str

def analyze_node(state):
    df = pd.read_csv(state["csv_file"])

    state["summary"] = df.to_string()

    return state

def insight_node(state):

    prompt = f"""
    Analyze the following dataset:

    {state['summary']}

    Give 5 important insights from the data.
    """

    response = model.generate_content(prompt)

    state["insights"] = response.text

    return state
def qa_node(state):

    prompt = f"""
    Dataset:

    {state['summary']}

    Insights:

    {state['insights']}

    User Question:

    {state['question']}

    Answer accurately based on the dataset.
    """

    response = model.generate_content(prompt)

    state["answer"] = response.text

    return state
