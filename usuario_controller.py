from app.models.usuario import Usuario
from app import db

class UsuarioController:
    @staticmethod
    def get_all():
        return Usuario.query.all()

    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)

    @staticmethod
    def create(data):
        novo_usuario = Usuario(**data)
        db.session.add(novo_usuario)
        db.session.commit()
        return novo_usuario

    @staticmethod
    def update(id, data):
        usuario = Usuario.query.get(id)
        for key, value in data.items():
            setattr(usuario, key, value)
        db.session.commit()
        return usuario

    @staticmethod
    def delete(id):
        usuario = Usuario.query.get(id)
        db.session.delete(usuario)
        db.session.commit()
        return usuario