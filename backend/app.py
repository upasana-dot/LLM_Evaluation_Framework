from flask import Flask, request, jsonify
from flask_cors import CORS

from pipeline import evaluate_prompt

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return {
        "message": "LLM Evaluation Framework API Running"
    }


@app.route("/evaluate", methods=["POST"])
def evaluate():

    data = request.get_json()

    prompt = data.get("prompt")

    if not prompt:
        return jsonify({
            "error": "Prompt is required."
        }), 400

    report = evaluate_prompt(prompt)

    return jsonify(report)


if __name__ == "__main__":
    app.run(debug=True, port=5002)