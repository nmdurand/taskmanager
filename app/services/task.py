from app.models.task import Task, db


class TaskService:
    def add_task(data):
        task = Task(title=data["title"])
        db.session.add(task)
        db.session.commit()

        return TaskService.get_task(task.id)

    def get_tasks():
        return Task.query.all()

    def get_task(_id):
        return Task.query.get(_id)

    def update_task(_id, _title):
        task = Task.query.get(_id)
        task.title = _title
        db.session.commit()

        return TaskService.get_task(task.id)

    def delete_task(_id):
        task = Task.query.get(_id)
        db.session.delete(task)
        db.session.commit()
