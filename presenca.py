from app import db

class Presenca(db.Model):
    __tablename__ = 'Presenca'

    id_presenca = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_aluno = db.Column(db.Integer, db.ForeignKey('Aluno.id_aluno'), nullable=False)
    data_presenca = db.Column(db.Date, nullable=False)
    presente = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Presenca {self.id_presenca}>'