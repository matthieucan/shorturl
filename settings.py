import os

app_folder = os.getcwd()

# the database uri, db backend has to be compatible with SQLAlchemy
DATABASE_URI = "sqlite:///" + os.path.join(app_folder, "data/db.sqlite")

# short url prefix, normally the url of your server
# should end with a slash
SHORT_URL_PREFIX = "http://127.0.0.1:5000/"
