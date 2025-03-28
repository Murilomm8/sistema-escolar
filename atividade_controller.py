from app.models.atividade import Atividade
from app import db

class AtividadeController:
    @staticmethod
    def get_all():
        return Atividade.query.all()

    @staticmethod
    def get_by_id(id):
        return Atividade.query.get(id)

    @staticmethod
    def create(data):
        nova_atividade = Atividade(**data)
        db.session.add(nova_atividade)
        db.session.commit()
        return nova_atividade

    @staticmethod
    def update(id, data):
        atividade = Atividade.query.get(id)
        for key, value in data.items():
            setattr(atividade, key, value)
        db.session.commit()
        return atividade

    @staticmethod
    def delete(id):
        atividade = Atividade.query.get(id)
        db.session.delete(atividade)
        db.session.commit()
        return atividade