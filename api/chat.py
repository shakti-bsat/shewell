from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    return jsonify({"response": "ok"})

# Required for Vercel
app = app
