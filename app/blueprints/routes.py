from flask import Blueprint, render_template
from app.models.tasks import Task

taskmanager_routes = Blueprint(
    "taskmanager_routes", __name__, template_folder="templates"
)


@taskmanager_routes.route("/")
def index():
    return render_template(f"index.html", tasks=Task.get_all_tasks())
