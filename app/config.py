from os import path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

SQLALCHEMY_DATABASE_URI = "sqlite:///taskmanager.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
