from flask import Blueprint, jsonify, request
from app.controllers.presenca_controller import PresencaController

presenca_bp = Blueprint('presenca', __name__)

@presenca_bp.route('/presencas', methods=['GET'])
def get_presencas():
    presencas = PresencaController.get_all()
    return jsonify([presenca.__dict__ for presenca in presencas])

@presenca_bp.route('/presencas/<int:id>', methods=['GET'])
def get_presenca(id):
    presenca = PresencaController.get_by_id(id)
    return jsonify(presenca.__dict__) if presenca else ('Presença não encontrada', 404)

@presenca_bp.route('/presencas', methods=['POST'])
def create_presenca():
    data = request.json
    presenca = PresencaController.create(data)
    return jsonify(presenca.__dict__), 201

@presenca_bp.route('/presencas/<int:id>', methods=['PUT'])
def update_presenca(id):
    data = request.json
    presenca = PresencaController.update(id, data)
    return jsonify(presenca.__dict__)

@presenca_bp.route('/presencas/<int:id>', methods=['DELETE'])
def delete_presenca(id):
    presenca = PresencaController.delete(id)
    return ('Presença removida com sucesso', 200)