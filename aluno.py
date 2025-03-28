from app import db

class Aluno(db.Model):
    __tablename__ = 'Aluno'

    id_aluno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_completo = db.Column(db.String(255), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    id_turma = db.Column(db.Integer, db.ForeignKey('Turma.id_turma'))
    nome_responsavel = db.Column(db.String(255), nullable=False)
    telefone_responsavel = db.Column(db.String(20))
    email_responsavel = db.Column(db.String(100))
    informacoes_adicionais = db.Column(db.Text)

    def __repr__(self):
        return f'<Aluno {self.nome_completo}>'