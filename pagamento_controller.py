from app.models.pagamento import Pagamento
from app import db

class PagamentoController:
    @staticmethod
    def get_all():
        return Pagamento.query.all()

    @staticmethod
    def get_by_id(id):
        return Pagamento.query.get(id)

    @staticmethod
    def create(data):
        novo_pagamento = Pagamento(**data)
        db.session.add(novo_pagamento)
        db.session.commit()
        return novo_pagamento

    @staticmethod
    def update(id, data):
        pagamento = Pagamento.query.get(id)
        for key, value in data.items():
            setattr(pagamento, key, value)
        db.session.commit()
        return pagamento

    @staticmethod
    def delete(id):
        pagamento = Pagamento.query.get(id)
        db.session.delete(pagamento)
        db.session.commit()
        return pagamento