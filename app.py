import streamlit as st
import pandas as pd

st.title("📚 Vocabulary List Viewer")

# Sample vocabulary data
data = {
    "Word": ["analyze", "construct", "define", "evaluate"],
    "Part of Speech": ["verb", "verb", "verb", "verb"],
    "Example": [
        "Please analyze the text.",
        "The students construct a model.",
        "Can you define this term?",
        "We evaluate the results together."
    ]
}

df = pd.DataFrame(data)
st.dataframe(df)
