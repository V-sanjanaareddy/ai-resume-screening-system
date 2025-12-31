# AI-Powered Resume Screening System

## Overview
This project is an AI-based resume classification system that categorizes resumes into job roles using Natural Language Processing and Machine Learning.

## Problem Statement
Recruiters often receive thousands of resumes. This system helps automate resume screening by classifying resumes into relevant job categories.

## Tech Stack
- Python
- Scikit-learn
- NLP (TF-IDF)
- Flask
- REST API

## Architecture
- TF-IDF for text vectorization
- Logistic Regression for classification
- Flask API for predictions

## How to Run

Step 1: Install Dependencies
pip install -r requirements.txt

Step 2: Train the Model
cd model
python train_model.py

This will generate:
resume_classifier.pkl

Step 3: Run the API
cd ../app
python app.py

The API will start at:
http://127.0.0.1:5000

### Train Model

```bash

API Usage
Endpoint
POST /predict

Sample API Request
{
  "resume_text": "Experienced in Python, machine learning and NLP"
}

Sample API Response

{
  "predicted_category": "Machine Learning"
}


What I Learned

Text preprocessing using TF-IDF

Building ML pipelines

Model training and evaluation

Saving and loading ML models

Deploying ML models using Flask REST APIs

Designing end-to-end AI systems




ai-resume-screening-system/
├── data/
├── model/
├── app/
├── notebooks/
├── requirements.txt
└── README.md

