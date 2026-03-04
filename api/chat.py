from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    return jsonify({"response": f"You said: {message}"})

# IMPORTANT: This must exist for Vercel
handler = app
