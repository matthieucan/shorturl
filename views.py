from flask import redirect, url_for, request, render_template

from app import app
import excepts
from url import base_conv
from db import session
from models import Url

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
       if "url" in request.form:
           try:
               # stores the url:
               Url(request.form["url"]).store()
           except:
               return undefined_error()
    
    return render_template("index.html", list=session.query(Url).all())

@app.route("/<encoded_url>")
def redir(encoded_url):
    try:
        id = base_conv(encoded_url, input_base=62, output_base=10)
        url = Url.retrieve(id)
        return redirect(url.long_url)
    except excepts.NotFoundException:
        return notfound_error()
    except:
        return undefined_error()

# error handlers

@app.errorhandler(500)
def server_error():
    return render_template("500.html")

@app.errorhandler(404)
def notfound_error():
    return render_template("404.html")

def undefined_error():
    return render_template("undefined_error.html")
