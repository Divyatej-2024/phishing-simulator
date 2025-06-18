
from flask import Flask, render_template, jsonify
import json, os

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/simulate/<attack_type>')
def simulate(attack_type):
    path = f'backend/attacks/{attack_type}.json'
    if os.path.exists(path):
        with open(path) as f:
            data = json.load(f)
        return jsonify(data)
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
