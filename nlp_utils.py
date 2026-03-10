import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop]
    return " ".join(tokens)

def missing_keywords(resume, job):
    resume_words = set(resume.split())
    job_words = set(job.split())

    missing = job_words - resume_words
    return list(missing)[:15]
