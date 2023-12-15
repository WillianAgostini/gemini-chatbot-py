import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    print("Please set GOOGLE_API_KEY in .env file")
    exit(1)

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')

def ask_question(question):
    response = model.generate_content(question)
    return response.text
