import streamlit as st
from parser import extract_resume_text
from nlp_utils import preprocess, missing_keywords
from similarity import similarity_score

st.title("AI Resume Analyzer by Matthew Wisnewski")

resume_file = st.file_uploader("Upload Resume (PDF)")
job_desc = st.text_area("Paste Job Description")

if resume_file and job_desc:

    resume_text = extract_resume_text(resume_file)

    processed_resume = preprocess(resume_text)
    processed_job = preprocess(job_desc)

    score = similarity_score(processed_resume, processed_job)

    missing = missing_keywords(processed_resume, processed_job)

    st.subheader(f"Match Score: {score}%")

    st.subheader("Missing Keywords")
    st.write(missing)
