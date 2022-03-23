from flask import Blueprint, request, Response, jsonify
from app.models.tasks import Task

taskmanager_api = Blueprint("taskmanager_api", __name__, url_prefix="/api")


@taskmanager_api.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"Tasks": Task.get_all_tasks()})


@taskmanager_api.route("/task/<int:id>", methods=["GET"])
def get_task_by_id(id):
    return_value = Task.get_task(id)
    return jsonify(return_value)


@taskmanager_api.route("/task", methods=["POST"])
def add_task():
    request_data = request.get_json()
    Task.add_task(request_data["title"])
    response = Response("Task added", 201, mimetype="application/json")
    return response


@taskmanager_api.route("/task/<int:id>", methods=["PUT"])
def update_task(id):
    request_data = request.get_json()
    Task.update_task(id, request_data["title"])
    response = Response("Task Updated", status=200, mimetype="application/json")
    return response


@taskmanager_api.route("/task/<int:id>", methods=["DELETE"])
def remove_task(id):
    Task.delete_task(id)
    response = Response("Task Deleted", status=200, mimetype="application/json")
    return response
