from flask import Blueprint, request
from marshmallow import Schema, fields, ValidationError
from app.services.task import TaskService

taskmanager_api = Blueprint("taskmanager_api", __name__, url_prefix="/api")


class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


@taskmanager_api.route("/tasks", methods=["GET"])
def get_tasks():
    return {"tasks": tasks_schema.dump(TaskService.get_tasks())}


@taskmanager_api.route("/task/<int:id>", methods=["GET"])
def get_task_by_id(id):
    return task_schema.dump(TaskService.get_task(id))


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
        return result, 201
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
        return result, 200
    except:
        return "Internal server error", 500


@taskmanager_api.route("/task/<int:id>", methods=["DELETE"])
def remove_task(id):
    try:
        TaskService.delete_task(id)
        return {"message": "Task deleted"}, 200
    except:
        return "Internal server error", 500
