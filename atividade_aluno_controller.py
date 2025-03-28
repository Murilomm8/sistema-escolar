from app.models.atividade_aluno import AtividadeAluno
from app import db

class AtividadeAlunoController:
    @staticmethod
    def get_all():
        return AtividadeAluno.query.all()

    @staticmethod
    def get_by_id(id_atividade, id_aluno):
        return AtividadeAluno.query.get((id_atividade, id_aluno))

    @staticmethod
    def create(data):
        nova_relacao = AtividadeAluno(**data)
        db.session.add(nova_relacao)
        db.session.commit()
        return nova_relacao

    @staticmethod
    def delete(id_atividade, id_aluno):
        relacao = AtividadeAluno.query.get((id_atividade, id_aluno))
        db.session.delete(relacao)
        db.session.commit()
        return relacao