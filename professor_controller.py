from app.models.professor import Professor
from app import db

class ProfessorController:
    @staticmethod
    def get_all():
        return Professor.query.all()

    @staticmethod
    def get_by_id(id):
        return Professor.query.get(id)

    @staticmethod
    def create(data):
        novo_professor = Professor(**data)
        db.session.add(novo_professor)
        db.session.commit()
        return novo_professor

    @staticmethod
    def update(id, data):
        professor = Professor.query.get(id)
        for key, value in data.items():
            setattr(professor, key, value)
        db.session.commit()
        return professor

    @staticmethod
    def delete(id):
        professor = Professor.query.get(id)
        db.session.delete(professor)
        db.session.commit()
        return professor