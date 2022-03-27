import os
from os import path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

db_path = os.environ.get("DATABASE_PATH")
if not path.exists(db_path):
    os.makedirs(db_path)

db_scheme = os.environ.get("DATABASE_SCHEME")
db_path = os.environ.get("DATABASE_PATH")
db_name = os.environ.get("DATABASE_NAME")

SQLALCHEMY_DATABASE_URI = f"{db_scheme}/{path.join(db_path, db_name)}"
print("Using db URL:", SQLALCHEMY_DATABASE_URI)
SQLALCHEMY_TRACK_MODIFICATIONS = False
