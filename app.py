from flask import Flask, redirect, url_for, request, render_template

import data, url, excepts

app = Flask(__name__)

@app.route("/<encoded_url>")
def redir(encoded_url):
    try:
        url = data.retrieve(encoded_url)
    except excepts.NotFoundException:
        return notfound_error()
    except:
        return undefined_error()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
       if "url" in request.form:
           try:
               encoded_url = url.encode(url) # encoding the url...
               data.store(url, encoded_url)  # ... and storing it
           except:
               return undefined_error()
    
    return render_template("index.html")

# error handlers

@app.errorhandler(500)
def server_error():
    return render_template("500.html")

@app.errorhandler(404)
def notfound_error():
    return render_template("404.html")

def undefined_error():
    return render_template("undefined_error.html")
