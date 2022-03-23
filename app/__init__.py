from flask import Flask

from app.blueprints.routes import taskmanager_routes
from app.blueprints.api import taskmanager_api


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile("config.py")

    from app.models.tasks import db

    db.init_app(app)

    app.register_blueprint(taskmanager_routes)
    app.register_blueprint(taskmanager_api)

    with app.app_context():
        db.create_all()

        return app
