from flask import Flask

app = Flask(__name__)

import views

from db import session

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()
