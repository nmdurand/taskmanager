from flask import Blueprint, render_template
from app.services.task import TaskService

taskmanager_views = Blueprint(
    "taskmanager_views", __name__, template_folder="templates"
)


@taskmanager_views.route("/")
def index():
    return render_template(f"index.html", tasks=TaskService.get_tasks())
