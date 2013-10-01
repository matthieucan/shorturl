from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route("/<url>")
def redir(url):
    try:
        return(redirect(decode(url)))
    except:
        return(redirect(url_for("index")))

@app.route("/", methods=["GET", "POST"])
def index():
    #if request.method == "POST":
    #    if "url" in request.form:
    #        return template(short=encode(request.form["url"]))

    return render_template("index.html")
