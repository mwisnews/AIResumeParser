# AI Resume Analyzer

An AI-powered resume analysis tool that evaluates how well a resume matches a job description. The application uses Natural Language Processing (NLP) and sentence embeddings to calculate similarity scores, identify missing keywords, and provide insights into resume-job compatibility.

The application runs locally through a simple Streamlit web interface where users can upload a resume and paste a job description to receive instant feedback.

## Features

- Upload and analyze PDF resumes

- Compare resume content with a job description

- Generate a match score using semantic similarity

- Identify missing keywords from the job description

- Clean and preprocess text using NLP techniques

- Interactive web interface built with Streamlit

## Technologies Used

| Technology | Purpose |
| --- | --- |
| Python | Core programming language |
| Streamlit | Web interface |
| spaCy | Natural language processing |
| Sentence Transformers | Text embeddings |
| Scikit-learn | Similarity scoring |
| pdfplumber | Resume PDF parsing |

## Project Structure

| File | Description |
| --- | --- |
| app.py | Main Streamlit application |
| parser.py | Resume file parsing |
| nlp_utils.py | NLP preprocessing and keyword extraction |
| similarity.py | Embeddings and similarity scoring |
| requirements.txt | Project dependencies |


## Installation


1. Clone the repository

`git clone https://github.com/mwisnews/AIResumeParser.git`

`cd AIResumeParser`

2. Create a virtual environment (recommended)

Mac/Linux

`python3 -m venv venv`

`source venv/bin/activate`

Windows

`python -m venv venv`

`venv\Scripts\activate`

3. Install dependencies
`pip install -r requirements.txt`
4. Install the spaCy language model
`python -m spacy download en_core_web_sm`

## Running the Application

Start the Streamlit server:

`streamlit run app.py`

After launching, open the browser at:

`http://localhost:8501`

<img width="1920" height="960" alt="Output" src="https://github.com/user-attachments/assets/2f6486c4-21b8-4d0c-90fc-bed48810e33a" />


## License

This project is intended for educational and portfolio purposes.


