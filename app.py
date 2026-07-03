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