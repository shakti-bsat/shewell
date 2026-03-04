from flask import Flask, request, jsonify
import os
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_query = data.get("query", "")

    if not user_query:
        return jsonify({"answer": "Please ask a question."})

    response = model.generate_content(user_query)

    return jsonify({
        "answer": response.text
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
