import streamlit as st
import pandas as pd
import requests
import io

st.title("📘 English Quiz from CSV")

# --- STEP 1: Load TSV (tab-separated) CSV from GitHub ---
csv_url = "https://raw.githubusercontent.com/MK316/YourRepo/main/quiz_questions.csv"  # use .tsv if applicable

try:
    response = requests.get(csv_url)
    response.raise_for_status()
    
    # ✅ Use sep='\t' for tab-separated files
    df = pd.read_csv(io.StringIO(response.text), sep='\t')

    # ✅ Normalize column names
    df.columns = df.columns.str.strip().str.replace(" ", "").str.capitalize()

except Exception as e:
    st.error(f"❌ Failed to load quiz data: {e}")
    st.stop()

# --- STEP 2: Display Quiz Questions ---
st.header("🧠 Take the Quiz")

if df.empty:
    st.warning("The quiz file is empty or incorrectly formatted.")
else:
    for idx, row in df.iterrows():
        question = row["Question"]
        options = [row[f"Option{i}"] for i in range(1, 6)]
        correct_answer = row["Answer"]

        st.subheader(f"Q{idx+1}: {question}")
        user_choice = st.radio("Choose one:", options, key=f"q_{idx}")

        if st.button("Check Answer", key=f"check_{idx}"):
            if user_choice == correct_answer:
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Not quite. The correct answer is **{correct_answer}**")
