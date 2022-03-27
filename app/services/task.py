from app.models.task import Task, db


class TaskService:
    def add_task(_title):
        new_task = Task(title=_title)
        db.session.add(new_task)
        db.session.commit()

    def get_all_tasks():
        return [Task.json(task) for task in Task.query.all()]

    def get_task(_id):
        return [Task.json(Task.query.filter_by(id=_id).first())]

    def update_task(_id, _title):
        task_to_update = Task.query.filter_by(id=_id).first()
        task_to_update.title = _title
        db.session.commit()

    def delete_task(_id):
        Task.query.filter_by(id=_id).delete()
        db.session.commit()
