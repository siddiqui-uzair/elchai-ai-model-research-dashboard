import streamlit as st
import pandas as pd


APP_TITLE = "Elchai AI Model Research Dashboard"

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🤖",
    layout="wide"
)

st.title(APP_TITLE)

st.write(
    "A beginner research dashboard comparing open-source AI models for "
    "Elchai Group business workflow use cases."
)

st.info("Selected model for limited internal testing: Qwen")

model_data = [
    {
        "Model": "Qwen",
        "Best For": "Internal assistants, document tasks, local testing, workflow support",
        "Strength": "Open-source model family, practical for business AI workflows",
        "Main Risk": "Needs testing for accuracy, privacy, and integration reliability",
        "Recommendation": "Test first"
    },
    {
        "Model": "Kimi",
        "Best For": "Long-context research, coding, agent-style tasks",
        "Strength": "Strong long-context and agentic workflow potential",
        "Main Risk": "Access, reliability, and claims need practical validation",
        "Recommendation": "Research further"
    },
    {
        "Model": "MiniMax",
        "Best For": "Conversational AI, content generation, multimodal use cases",
        "Strength": "Useful for customer-facing and creative AI workflows",
        "Main Risk": "Business fit and privacy controls need testing",
        "Recommendation": "Monitor"
    },
    {
        "Model": "GLM",
        "Best For": "General AI assistant, research, coding support",
        "Strength": "Open model ecosystem with general-purpose capabilities",
        "Main Risk": "Requires evaluation against Elchai workflow needs",
        "Recommendation": "Compare later"
    }
]

df = pd.DataFrame(model_data)

st.header("Model Comparison")
st.dataframe(df, use_container_width=True)

st.header("Use Case Recommendation")

use_case = st.selectbox(
    "Select an Elchai business use case",
    [
        "Internal research assistant",
        "Project coordination support",
        "Document summarization",
        "Coding and product support",
        "Local/private AI assistant"
    ]
)

recommendations = {
    "Internal research assistant": {
        "Model": "Qwen",
        "Why": "Good starting point for summarizing research notes and supporting internal knowledge workflows.",
        "Departments": "Strategy, Product, Operations"
    },
    "Project coordination support": {
        "Model": "Qwen",
        "Why": "Can help convert project notes into summaries, action points, and follow-up items.",
        "Departments": "Operations, Product, Strategy"
    },
    "Document summarization": {
        "Model": "Qwen",
        "Why": "Suitable for testing document-based workflows in a controlled internal environment.",
        "Departments": "Operations, Finance, Strategy"
    },
    "Coding and product support": {
        "Model": "Kimi",
        "Why": "Promising for longer coding and agent-style tasks, but should be tested carefully first.",
        "Departments": "Engineering, Product, IT/Infrastructure"
    },
    "Local/private AI assistant": {
        "Model": "Qwen",
        "Why": "More suitable for local or controlled testing compared to fully external tools.",
        "Departments": "IT/Infrastructure, Operations"
    }
}

selected = recommendations[use_case]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Recommended Model", selected["Model"])

with col2:
    st.metric("Testing Stage", "Limited Pilot")

with col3:
    st.metric("Data Type", "Non-confidential")

st.subheader("Why this model fits")
st.write(selected["Why"])

st.subheader("Departments that may benefit")
st.write(selected["Departments"])

st.header("Risks and Limitations")

risks = [
    "Privacy risk if confidential company or client data is used",
    "Security review needed before connecting to internal systems",
    "AI output may be inaccurate or incomplete",
    "Local hardware cost may be high for larger models",
    "Integration with existing workflows may take time",
    "Human review is required before using AI-generated outputs"
]

for risk in risks:
    st.write(f"- {risk}")

st.header("Final Recommendation")

st.success(
    "Recommendation: Test Qwen first in a limited internal proof-of-concept using "
    "non-confidential data. Avoid production use until privacy, security, accuracy, "
    "integration, and reliability risks are reviewed."
)