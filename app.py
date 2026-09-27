from flask import Flask, render_template, request, jsonify
from agent import diagnose_with_memory
from memory import store_incident

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/diagnose", methods=["POST"])
def diagnose():
    incident_text = request.json["incident"]
    result = diagnose_with_memory(incident_text)
    return jsonify({"response": result.text})

if __name__ == "__main__":
    app.run(debug=False, port=5000, threaded=False)