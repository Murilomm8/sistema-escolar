from app import db

class Professor(db.Model):
    __tablename__ = 'Professor'

    id_professor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_completo = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Professor {self.nome_completo}>'