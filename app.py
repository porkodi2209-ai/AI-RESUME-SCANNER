import streamlit as st
import pdfplumber

st.title("AI Resume Analyzer")

file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()
    return text

skills = ["python", "java", "sql", "machine learning",
          "data science", "html", "css", "javascript"]

if file:
    text = extract_text(file)

    st.subheader("Resume Content")
    st.write(text)

    found = [s for s in skills if s in text.lower()]
    missing = [s for s in skills if s not in found]

    st.subheader("Skills Found")
    st.write(found)

    score = (len(found)/len(skills))*100
    st.subheader("ATS Score")
    st.write(f"{round(score,2)} %")

    st.subheader("Missing Skills")
    st.write(missing)