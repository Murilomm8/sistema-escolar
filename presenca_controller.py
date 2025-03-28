from app.models.presenca import Presenca
from app import db

class PresencaController:
    @staticmethod
    def get_all():
        return Presenca.query.all()

    @staticmethod
    def get_by_id(id):
        return Presenca.query.get(id)

    @staticmethod
    def create(data):
        nova_presenca = Presenca(**data)
        db.session.add(nova_presenca)
        db.session.commit()
        return nova_presenca

    @staticmethod
    def update(id, data):
        presenca = Presenca.query.get(id)
        for key, value in data.items():
            setattr(presenca, key, value)
        db.session.commit()
        return presenca

    @staticmethod
    def delete(id):
        presenca = Presenca.query.get(id)
        db.session.delete(presenca)
        db.session.commit()
        return presenca