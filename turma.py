from app import db

class Turma(db.Model):
    __tablename__ = 'Turma'

    id_turma = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_turma = db.Column(db.String(50), nullable=False)
    id_professor = db.Column(db.Integer, db.ForeignKey('Professor.id_professor'), nullable=False)
    horario = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Turma {self.nome_turma}>'