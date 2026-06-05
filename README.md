# 🤖 Multi-Agent Research Assistant

## Application Preview

![Application Screenshot](ScreenshotAIAPP.png)



## Overview

The Multi-Agent Research Assistant is an AI-powered research automation system built using Python, Streamlit, Groq LLM, and DuckDuckGo Search.

The system uses multiple specialized AI agents to automate the complete research workflow, including planning, information gathering, analysis, report generation, review, and memory management.

---

## Features

* Automated research planning
* Web information retrieval
* AI-powered research analysis
* Professional report generation
* Report review and refinement
* Memory storage for previous research
* Interactive Streamlit user interface

---

## Multi-Agent Workflow

```text
User Query
    ↓
Planner Agent
    ↓
Search Agent
    ↓
Research Agent
    ↓
Analyst Agent
    ↓
Writer Agent
    ↓
Reviewer Agent
    ↓
Memory Agent
    ↓
Final Research Report
```

---

## Technologies Used

* Python
* Streamlit
* Groq API
* DuckDuckGo Search (DDGS)
* JSON Storage
* Pandas
* Matplotlib

---

## Project Structure

```text
MultiAgentResearchAssistant/
│
├── agents/
│   ├── planner.py
│   ├── search_agent.py
│   ├── researcher.py
│   ├── analyst.py
│   ├── writer.py
│   ├── reviewer.py
│   └── memory_agent.py
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   └── reports/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/birajkumarbhol/MultiAgentResearchAssistant.git
cd MultiAgentResearchAssistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment File

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### Run Application

```bash
streamlit run app/streamlit_app.py
```

---

## Example Workflow

1. User enters a research topic.
2. Planner Agent creates a research plan.
3. Search Agent collects web information.
4. Research Agent extracts key insights.
5. Analyst Agent performs detailed analysis.
6. Writer Agent generates a professional report.
7. Reviewer Agent validates output quality.
8. Memory Agent stores research history.

---

## Future Improvements

* Data visualization dashboards
* Image-based search results
* PDF report export
* LangGraph integration
* Cloud deployment
* Advanced memory management

---

## Author

**Biraj Kumar Bhol**

AI Engineer | Machine Learning Enthusiast | Python Developer
