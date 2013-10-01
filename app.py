from flask import Flask, redirect, url_for, request, render_template

import data, url

app = Flask(__name__)

@app.route("/<encoded_url>")
def redir(encoded_url):
    try:
        url = data.retrieve(encoded_url)
    except:
        return(redirect(url_for("404")))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
       if "url" in request.form:
           encoded_url = url.encode(url) # encoding the url...
           data.store(url, encoded_url)  # ... and storing it
           

    return render_template("index.html")
