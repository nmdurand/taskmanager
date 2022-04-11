from marshmallow import Schema, fields, ValidationError

from app.models.task import Task, db


class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


class TaskService:
    def add_task(data):
        task = Task(title=data["title"])
        db.session.add(task)
        db.session.commit()

        return TaskService.get_task(task.id)

    def get_tasks():
        tasks = Task.query.all()

        return tasks_schema.dump(tasks)

    def get_task(_id):
        task = Task.query.get(_id)

        return task_schema.dump(task)

    def update_task(_id, _title):
        task = Task.query.get(_id)
        task.title = _title
        db.session.commit()

        return TaskService.get_task(task.id)

    def delete_task(_id):
        task = Task.query.get(_id)
        db.session.delete(task)
        db.session.commit()
