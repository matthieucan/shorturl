from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route("/<url>")
def redir(url):
    try:
        return(redirect(decode(url)))
    except:
        return(redirect(url_for("index")))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "url" in request.form:
            return template(short=encode(request.form["url"]))

    return template()

def template(short=None):
    if short is None:
        return """
<form action="." method="post" name="form">
  <input type="text" name="url" />
  <input type="submit" value="Short it!" />
</form>
"""
    else:
        return short

if __name__ == "__main__":
    app.run(debug=True)
