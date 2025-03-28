from app.models.aluno import Aluno
from app import db

class AlunoController:
    @staticmethod
    def get_all():
        return Aluno.query.all()

    @staticmethod
    def get_by_id(id):
        return Aluno.query.get(id)

    @staticmethod
    def create(data):
        novo_aluno = Aluno(**data)
        db.session.add(novo_aluno)
        db.session.commit()
        return novo_aluno

    @staticmethod
    def update(id, data):
        aluno = Aluno.query.get(id)
        for key, value in data.items():
            setattr(aluno, key, value)
        db.session.commit()
        return aluno

    @staticmethod
    def delete(id):
        aluno = Aluno.query.get(id)
        db.session.delete(aluno)
        db.session.commit()
        return aluno