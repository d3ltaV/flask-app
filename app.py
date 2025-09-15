from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__, template_folder="template")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get-fact")
def get_fact():
    response = requests.get("https://catfact.ninja/fact")
    data = response.json()
    fact = data["fact"]
    return render_template("fact.html", f=fact)

@app.route("/dog-image")
def dog_img():
    n = request.args.get("num")
    if n == "":
        n = 1
    num = int(n)
    response = requests.get(f"https://dog.ceo/api/breeds/image/random/{num}")
    data = response.json()
    dog_img = data["message"]
    return render_template("dog.html", img=dog_img)

if __name__ == "__main__":
    app.run(debug=True)