import streamlit as st


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