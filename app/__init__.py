from flask import Flask

from app.models.tasks import db
from app.blueprints.views import taskmanager_views
from app.blueprints.api import taskmanager_api


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile("config.py")

    db.init_app(app)
    db.create_all(app=app)

    app.register_blueprint(taskmanager_views)
    app.register_blueprint(taskmanager_api)

    return app
