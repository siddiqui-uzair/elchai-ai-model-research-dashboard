# Elchai AI Model Research Dashboard

A beginner Streamlit dashboard created for the Elchai Group AI Agent & OpenClaw Research Intern assessment.

The project compares open-source AI models mentioned in the assessment task, including Qwen, Kimi, MiniMax, and GLM. It maps these models to possible Elchai Group business workflow use cases, departments, risks, and adoption recommendations.

## Selected Model

The selected model for limited internal testing is **Qwen**.

Qwen was selected because it is an open source model family that may be useful for internal AI workflows such as research support, document summarization, project coordination, and local/private AI assistant testing.

## What This Dashboard Shows

- Comparison of Qwen, Kimi, MiniMax, and GLM
- Best fit use cases for each model
- Business use case selector
- Recommended model for each use case
- Departments that may benefit
- Risks and limitations
- Final recommendation for safe testing

## Tech Used

- Python
- Streamlit
- pandas

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
streamlit run app.py

Final Recommendation

Test Qwen first in a limited internal proof of concept using non confidential data.

It should not be used in production or with sensitive client/company data until privacy, security, accuracy, integration, and reliability risks are reviewed.

Note

This is a beginner research dashboard and not a production AI system. It is intended as a small practical output for research, and comparison etc.