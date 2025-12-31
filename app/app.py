from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load trained model
with open("../model/resume_classifier.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    resume_text = data.get("resume_text")

    if not resume_text:
        return jsonify({"error": "Resume text is required"}), 400

    prediction = model.predict([resume_text])[0]

    return jsonify({"predicted_category": prediction})

if __name__ == "__main__":
    app.run(debug=True)
