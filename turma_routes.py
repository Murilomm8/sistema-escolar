from flask import Blueprint, jsonify, request
from app.controllers.turma_controller import TurmaController

turma_bp = Blueprint('turma', __name__)

@turma_bp.route('/turmas', methods=['GET'])
def get_turmas():
    turmas = TurmaController.get_all()
    return jsonify([turma.__dict__ for turma in turmas])

@turma_bp.route('/turmas/<int:id>', methods=['GET'])
def get_turma(id):
    turma = TurmaController.get_by_id(id)
    return jsonify(turma.__dict__) if turma else ('Turma não encontrada', 404)

@turma_bp.route('/turmas', methods=['POST'])
def create_turma():
    data = request.json
    turma = TurmaController.create(data)
    return jsonify(turma.__dict__), 201

@turma_bp.route('/turmas/<int:id>', methods=['PUT'])
def update_turma(id):
    data = request.json
    turma = TurmaController.update(id, data)
    return jsonify(turma.__dict__)

@turma_bp.route('/turmas/<int:id>', methods=['DELETE'])
def delete_turma(id):
    turma = TurmaController.delete(id)
    return ('Turma removida com sucesso', 200)