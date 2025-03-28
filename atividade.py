from app import db

class Atividade(db.Model):
    __tablename__ = 'Atividade'

    id_atividade = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.Text, nullable=False)
    data_realizacao = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Atividade {self.descricao}>'