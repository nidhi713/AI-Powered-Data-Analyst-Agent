# 🤖 AI Data Analyst Agent

An AI-powered data analysis application that allows users to upload CSV datasets, generate automated insights, visualize trends, and ask natural language questions about their data using Google's Gemini model.

## 🎥 Demo Video

[▶ Watch Project Demo](https://raw.githubusercontent.com/nidhi713/AI-Powered-Data-Analyst-Agent/main/demo.mp4)

## 🚀 Features

* 📂 CSV Dataset Upload
* 📊 Automatic Dataset Analysis
* 💡 AI-Generated Insights
* 📈 Data Visualization (Department-wise Salary Analysis)
* ❓ Natural Language Question Answering
* 🔄 LangGraph-Based Workflow Orchestration
* ⚡ Powered by Gemini 2.5 Flash

## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* Matplotlib
* LangGraph
* Google Gemini API
* Python Dotenv

## 🏗️ Architecture

Upload CSV
→ Analyze Dataset
→ Generate Insights
→ Answer User Questions
→ Visualize Results

## 📋 Workflow

### Analyze Node

Reads the CSV dataset and generates a structured summary.

### Insights Node

Uses Gemini to identify key trends and insights from the dataset.

### QA Node

Answers user questions using dataset context and generated insights.

## 📊 Example Use Cases

* Employee Salary Analysis
* Sales Data Exploration
* HR Analytics
* Customer Dataset Analysis
* Business Intelligence Reporting

## ▶️ Run Locally

```bash
git clone <repository-url>
cd AI-Data-Analyst-Agent

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```


## 🌟 Key Highlights

* Built an end-to-end AI Data Analysis workflow.
* Integrated Gemini LLM for intelligent data reasoning.
* Implemented LangGraph for workflow orchestration.
* Developed an interactive Streamlit interface.
* Automated insight generation and question answering from CSV datasets.
