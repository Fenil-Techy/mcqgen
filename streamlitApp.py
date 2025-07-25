import os
import json
import traceback
import re
from langchain_ollama import ChatOllama
from src.mcqgenerator.main import quiz_chain
from src.mcqgenerator.utils import read_file
import streamlit as st

st.set_page_config(page_title="MCQ Generator", page_icon=":book:", layout="wide")

with open(r"E:\mcqgen\Response.json", "r") as f:
    RESPONSE_JSON = json.load(f)

st.title("AI MCQ Generator")

if "quiz_dict" not in st.session_state:
    st.session_state.quiz_dict = None
    st.session_state.text = None

mode=st.radio("Select Mode", options=["File Upload", "Text Input"],index=0)
with st.form("User Inputs"):
    text = ""  # default
    if mode == "File Upload":
        file_upload = st.file_uploader("Upload a PDF or TXT file")
    else:
        file_upload = None
        text = st.text_area("Enter text here")
        
    mcq_number = st.number_input("Number of MCQs to generate", min_value=1, max_value=20, value=5)

    subject=st.text_input("Subject", value="Science")
    
    tone = st.selectbox("Tone", options=["Simple", "Intermediate", "Hard"], index=0)
    
    button=st.form_submit_button("Generate MCQs")

if button:
    with st.spinner("Generating MCQs..."):
        
        try:
            if mode == "File Upload":
                text = read_file(file_upload)
                if file_upload is None:
                    st.error("Please upload a file to generate MCQs.")
                    st.stop()
                    
            else:
                if not text:
                    st.error("Please enter some text to generate MCQs.")
                    st.stop()
            
        
            response = quiz_chain.invoke({
                
                "text": text,
                "number": mcq_number,
                "subject": subject,
                "tone": tone,
                "response_json": json.dumps(RESPONSE_JSON)
            })
                    
            st.subheader("Generated MCQs")
            quiz_content = response.content
            quiz_dict = json.loads(quiz_content)
            st.session_state.quiz_dict = quiz_dict
            
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)
            st.error(f"An error occurred: {e}")



if st.session_state.quiz_dict:
    st.subheader("Take the Quiz!")
    user_answers = {}
    score = 0

    with st.form("quiz_form"):
        for q_num, q_data in st.session_state.quiz_dict.items():
            st.write(f"**Q{q_num}: {q_data['mcq']}**")
            options = q_data['options']
            choices = [f"{k}: {v}" for k, v in options.items()]
            selected = st.radio(
                label="Select an option:",
                options=choices,
                key=f"q_{q_num}",
                index=None
            )
            if selected:
                
            # Save only 'a', 'b', etc.
                user_answers[q_num] = selected.split(":")[0]
            else:
                user_answers[q_num] = None
        submitted = st.form_submit_button("Submit Quiz")

    if submitted:
        st.subheader("Results:")
        for q_num, q_data in st.session_state.quiz_dict.items():
            correct = q_data['correct']
            user_ans = user_answers[q_num]
            if user_ans == correct:
                st.success(f"Q{q_num}: Correct ✅")
                score += 1
            else:
                st.error(f"Q{q_num}: Wrong ❌ (Correct: {correct})")

        st.write(f"### 📝 Your Score: {score} / {len(st.session_state.quiz_dict)}")
