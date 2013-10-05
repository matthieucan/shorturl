from flask import Flask

import settings

app = Flask(__name__)
app.config.from_object(settings)

import views

from db import session

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()
