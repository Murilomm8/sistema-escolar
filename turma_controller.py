from app.models.turma import Turma
from app import db

class TurmaController:
    @staticmethod
    def get_all():
        return Turma.query.all()

    @staticmethod
    def get_by_id(id):
        return Turma.query.get(id)

    @staticmethod
    def create(data):
        nova_turma = Turma(**data)
        db.session.add(nova_turma)
        db.session.commit()
        return nova_turma

    @staticmethod
    def update(id, data):
        turma = Turma.query.get(id)
        for key, value in data.items():
            setattr(turma, key, value)
        db.session.commit()
        return turma

    @staticmethod
    def delete(id):
        turma = Turma.query.get(id)
        db.session.delete(turma)
        db.session.commit()
        return turma