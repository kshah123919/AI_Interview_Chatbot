from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import Flask, request, jsonify
from flask_cors import CORS
from interview_agent import evaluate_ans  

app = Flask(__name__)
CORS(app)

@app.route("/interview", methods=["POST"])
def interview():
    data = request.json

    question = data.get("question")
    answer = data.get("answer")
    role = data.get("role")

   
    feedback_text = evaluate_ans(question, answer)

    return jsonify({
        "ai_reply": feedback_text
    })

if __name__ == "__main__":
    app.run(debug=True)
