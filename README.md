# AI-Powered Resume Screening System

## Overview
This project is an AI-based resume classification system that categorizes resumes
into job roles using Natural Language Processing (NLP) and Machine Learning.
It simulates how Applicant Tracking Systems (ATS) assist recruiters in screening resumes.

---

## Problem Statement
Recruiters often receive thousands of resumes for a single role.
Manual screening is time-consuming and inefficient.
This system automates resume screening by classifying resumes into relevant job categories.

---

## Tech Stack
- Python
- Pandas
- Scikit-learn
- NLP (TF-IDF)
- Flask
- REST API

---

## Architecture
- TF-IDF for text vectorization
- Logistic Regression for classification
- Flask REST API for serving predictions

---

## Project Structure
ai-resume-screening-system/
├── data/
│ └── resumes.csv
├── model/
│ ├── train_model.py
│ └── resume_classifier.pkl
├── app/
│ └── app.py
├── notebooks/
│ └── exploration.ipynb
├── requirements.txt
├── .gitignore
└── README.md


---

## How to Run the Project

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```
### Step 2: Train the Model
```bash
cd model
python train_model.py
```
This generates the trained model file:
resume_classifier.pkl

### Step 3: Run the API
```bash
cd ../app
python app.py
```
The API starts at:
http://127.0.0.1:5000


API Usage
Endpoint
```bash
POST /predict
```

Sample API Request

{
  "resume_text": "Experienced in Python, machine learning and NLP"
}

Sample API Response

{
  "predicted_category": "Machine Learning"
}

What I Learned:

Text preprocessing using TF-IDF

Building end-to-end ML pipelines

Training and evaluating classification models

Saving and loading trained ML models

Deploying ML models using Flask REST APIs

Designing real-world AI systems
