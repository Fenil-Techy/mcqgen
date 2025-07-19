import os
import json

import traceback
from src.mcqgenerator.logger import logging
from src.mcqgenerator.utils import read_file
from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate


llm = ChatOllama(model="llama3.1:8b")

TEMPLATE = """
Text: {text}

You are an expert MCQ maker. Given the above text, your task is to
create a quiz of {number} multiple-choice questions for {subject} students in a {tone} tone.
Ensure that:
- The questions are not repeated.
- All questions conform strictly to the content of the given text.
- The tone and difficulty match the intended audience.

⚠️ Important:
- Format your response exactly like the example RESPONSE_JSON below and use it as a guide.
- Return ONLY a valid JSON object in the specified format.
- Do NOT include any explanations, notes, or extra text. Only output the JSON.

Ensure to generate exactly {number} MCQs.

### RESPONSE_JSON
{response_json}
"""


quiz_generation_prompt = ChatPromptTemplate.from_messages([
   HumanMessagePromptTemplate.from_template(TEMPLATE)
    ])

quiz_chain = quiz_generation_prompt | llm
