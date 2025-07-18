from setuptools import setup, find_packages

setup(
    name='mcqgen',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'langchain',
        'streamlit',
        'python-dotenv',
        'PyPDF2',
        'langchain_ollama',  # or langchain_ollama in your case
    ]
)
