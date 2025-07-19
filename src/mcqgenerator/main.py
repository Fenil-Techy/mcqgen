import os
import json

import traceback
from src.mcqgenerator.logger import logging
from src.mcqgenerator.utils import read_file
from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate


llm = ChatOllama(model="llama3.1:8b")

TEMPLATE="""
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz  of {number} multiple choice questions for {subject} students in {tone} tone. 
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like  RESPONSE_JSON below  and use it as a guide and Return ONLY a valid JSON object in the following format. Do NOT include any explanations or other text. Just the JSON. \
Ensure to make {number} MCQs
### RESPONSE_JSON
{response_json}

"""

quiz_generation_prompt = ChatPromptTemplate.from_messages([
   HumanMessagePromptTemplate.from_template(TEMPLATE)
    ])

quiz_chain = quiz_generation_prompt | llm
