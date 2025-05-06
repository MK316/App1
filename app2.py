import streamlit as st
import pandas as pd

st.title("📝 English Word Quiz")

question = "What is the synonym of *happy*?"
options = ["angry", "sad", "joyful", "tired", "hungry"]
answer = "joyful"

# ✅ Display the question
st.markdown(question)

user_choice = st.radio("Choose the correct answer:", options)

if st.button("Check Answer"):
    if user_choice == answer:
        st.success("Correct!")
    else:
        st.error("Not quite. Try again.")

