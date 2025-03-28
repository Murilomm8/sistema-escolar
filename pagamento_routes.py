from flask import Blueprint, jsonify, request
from app.controllers.pagamento_controller import PagamentoController

pagamento_bp = Blueprint('pagamento', __name__)

@pagamento_bp.route('/pagamentos', methods=['GET'])
def get_pagamentos():
    pagamentos = PagamentoController.get_all()
    return jsonify([pagamento.__dict__ for pagamento in pagamentos])

@pagamento_bp.route('/pagamentos/<int:id>', methods=['GET'])
def get_pagamento(id):
    pagamento = PagamentoController.get_by_id(id)
    return jsonify(pagamento.__dict__) if pagamento else ('Pagamento não encontrado', 404)

@pagamento_bp.route('/pagamentos', methods=['POST'])
def create_pagamento():
    data = request.json
    pagamento = PagamentoController.create(data)
    return jsonify(pagamento.__dict__), 201

@pagamento_bp.route('/pagamentos/<int:id>', methods=['PUT'])
def update_pagamento(id):
    data = request.json
    pagamento = PagamentoController.update(id, data)
    return jsonify(pagamento.__dict__)

@pagamento_bp.route('/pagamentos/<int:id>', methods=['DELETE'])
def delete_pagamento(id):
    pagamento = PagamentoController.delete(id)
    return ('Pagamento removido com sucesso', 200)