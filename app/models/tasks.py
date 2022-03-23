from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()


class Task(db.Model):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
    )

    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

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
