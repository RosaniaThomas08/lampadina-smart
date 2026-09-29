from flask import render_template
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# stato della lampadina in memoria
lampadina = {
    "accesa": False,
    "colore": "#ffffff"
}

@app.route("/stato", methods=["GET"])
def get_stato():
    return jsonify(lampadina)

@app.route("/toggle", methods=["POST"])
def toggle():
    lampadina["accesa"] = not lampadina["accesa"]
    return jsonify(lampadina)

@app.route("/colore", methods=["POST"])
def set_colore():
    dati = request.get_json()
    lampadina["colore"] = dati.get("colore", lampadina["colore"])
    return jsonify(lampadina)

@app.route("/")
def home():
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)