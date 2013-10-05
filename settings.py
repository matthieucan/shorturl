import os

app_folder = os.getcwd()

DATABASE_URI = "sqlite:///" + os.path.join(app_folder, "data/db.sqlite")
