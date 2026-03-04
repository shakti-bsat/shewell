from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def chat():
    data = request.json
    return jsonify({"response": "ok"})

app = app
