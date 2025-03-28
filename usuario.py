from app import db

class Usuario(db.Model):
    __tablename__ = 'Usuario'

    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    nivel_acesso = db.Column(db.String(20), nullable=False)
    id_professor = db.Column(db.Integer, db.ForeignKey('Professor.id_professor'), nullable=True)

    def __repr__(self):
        return f'<Usuario {self.login}>'