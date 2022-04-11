from flask import Blueprint, request, Response, jsonify
from marshmallow import ValidationError
from app.services.task import TaskService, task_schema

taskmanager_api = Blueprint("taskmanager_api", __name__, url_prefix="/api")


@taskmanager_api.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": TaskService.get_tasks()})


@taskmanager_api.route("/task/<int:id>", methods=["GET"])
def get_task_by_id(id):
    return_value = TaskService.get_task(id)
    return jsonify(return_value)


@taskmanager_api.route("/task", methods=["POST"])
def add_task():
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    try:
        data = task_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 422

    try:
        result = TaskService.add_task(data)
        return {
            "message": "Added new task",
            "mimetype": "application/json",
            "task": result,
            "status": 201,
        }
    except:
        return "Internal server error", 500


@taskmanager_api.route("/task/<int:id>", methods=["PUT"])
def update_task(id):
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    try:
        data = task_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 422

    try:
        result = TaskService.update_task(id, data["title"])
        return {
            "message": "Updated task",
            "mimetype": "application/json",
            "task": result,
            "status": 200,
        }
    except:
        return "Internal server error", 500


@taskmanager_api.route("/task/<int:id>", methods=["DELETE"])
def remove_task(id):
    try:
        TaskService.delete_task(id)
        return {
            "message": "Task deleted",
            "mimetype": "application/json",
            "status": 200,
        }
    except:
        return "Internal server error", 500
