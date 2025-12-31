import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Load data
data = pd.read_csv("../data/resumes.csv")

X = data["resume_text"]
y = data["category"]

# Create ML pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("clf", LogisticRegression(max_iter=1000))
])

# Train model
pipeline.fit(X, y)

# Save model
with open("resume_classifier.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("Model trained and saved successfully.")
