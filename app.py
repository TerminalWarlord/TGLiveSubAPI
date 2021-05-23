from flask import Flask, jsonify
import requests
import tg

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def home():
    return "API is working"

@app.route("/<query>")
def tginfo(query):
    return jsonify(tg.telegram(query))

if __name__ == "__main__":

    app.run("0.0.0.0", port = 5000)