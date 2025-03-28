from flask import Blueprint, jsonify, request
from app.controllers.atividade_controller import AtividadeController

atividade_bp = Blueprint('atividade', __name__)

@atividade_bp.route('/atividades', methods=['GET'])
def get_atividades():
    atividades = AtividadeController.get_all()
    return jsonify([atividade.__dict__ for atividade in atividades])

@atividade_bp.route('/atividades/<int:id>', methods=['GET'])
def get_atividade(id):
    atividade = AtividadeController.get_by_id(id)
    return jsonify(atividade.__dict__) if atividade else ('Atividade não encontrada', 404)

@atividade_bp.route('/atividades', methods=['POST'])
def create_atividade():
    data = request.json
    atividade = AtividadeController.create(data)
    return jsonify(atividade.__dict__), 201

@atividade_bp.route('/atividades/<int:id>', methods=['PUT'])
def update_atividade(id):
    data = request.json
    atividade = AtividadeController.update(id, data)
    return jsonify(atividade.__dict__)

@atividade_bp.route('/atividades/<int:id>', methods=['DELETE'])
def delete_atividade(id):
    atividade = AtividadeController.delete(id)
    return ('Atividade removida com sucesso', 200)