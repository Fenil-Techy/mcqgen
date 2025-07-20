# 📚 AI-powered MCQ Generator

A simple, interactive **MCQ (Multiple Choice Questions) Generator** web app built with **Python, Streamlit, LangChain, and Ollama (LLM)**.

Users can:
- Upload a PDF or text file **OR type custom text**
- Generate a specified number of MCQs in a chosen tone & subject
- Take the quiz interactively
- See their score & correct answers

---

## 🚀 Features
- ✅ Upload `.pdf` or `.txt` files as input
- ✅ Or type your own text prompt
- ✅ Choose number of MCQs, subject & tone (Simple / Intermediate / Hard)
- ✅ Automatically generates MCQs using an LLM (e.g., Mistral / Llama3 with Ollama)
- ✅ Clean Streamlit UI
- ✅ Interactive quiz interface
- ✅ Score calculation & feedback

---

## 📁 Project Structure

mcqgen/
├── streamlitApp.py # Main Streamlit app
├── Response.json # Template JSON format for the output
├── requirements.txt # Python dependencies
├── src/
│ └── mcqgenerator/
│ ├── logger.py # Simple logger
│ ├── main.py # LangChain chains setup
│ ├── prompt.py # Prompt template
│ ├── utils.py # File reading utility
└── README.md

---

## 🧰 Tech Stack

- Python 3.10+
- Streamlit
- LangChain
- Ollama (running locally with Mistral or Llama3)
- PyPDF2 (to extract text from PDF)

---

## ⚙️ Setup & Run Locally

### 1️⃣ Clone the repository

git clone <your-repo-url>
cd mcqgen

### 2️⃣ Create virtual environment & install dependencies

python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On Linux/Mac

pip install -r requirements.txt

### 3️⃣ Start Ollama with a model

Download Ollama in your system

ollama run llama3

### 4️⃣ Run Streamlit app

streamlit run streamlitApp.py