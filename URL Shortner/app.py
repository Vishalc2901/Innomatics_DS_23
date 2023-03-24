from flask import Flask, render_template, request
import pyshorteners


app = Flask(__name__)


@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == "POST":
        url = request.form.get("url_name")
        sh = pyshorteners.Shortener() # Pyshortener object
        short_url = sh.tinyurl.short(url)
        return render_template("url.html", res = short_url, url=url)
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug = True)