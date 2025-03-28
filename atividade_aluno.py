from app import db

class AtividadeAluno(db.Model):
    __tablename__ = 'Atividade_Aluno'

    id_atividade = db.Column(db.Integer, db.ForeignKey('Atividade.id_atividade'), primary_key=True)
    id_aluno = db.Column(db.Integer, db.ForeignKey('Aluno.id_aluno'), primary_key=True)

    def __repr__(self):
        return f'<AtividadeAluno Atividade: {self.id_atividade}, Aluno: {self.id_aluno}>'