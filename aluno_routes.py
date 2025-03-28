from flask import Blueprint, jsonify, request
from app.controllers.aluno_controller import AlunoController

aluno_bp = Blueprint('aluno', __name__)

@aluno_bp.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = AlunoController.get_all()
    return jsonify([aluno.__dict__ for aluno in alunos])

@aluno_bp.route('/alunos/<int:id>', methods=['GET'])
def get_aluno(id):
    aluno = AlunoController.get_by_id(id)
    return jsonify(aluno.__dict__) if aluno else ('Aluno não encontrado', 404)

@aluno_bp.route('/alunos', methods=['POST'])
def create_aluno():
    data = request.json
    aluno = AlunoController.create(data)
    return jsonify(aluno.__dict__), 201

@aluno_bp.route('/alunos/<int:id>', methods=['PUT'])
def update_aluno(id):
    data = request.json
    aluno = AlunoController.update(id, data)
    return jsonify(aluno.__dict__)

@aluno_bp.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    aluno = AlunoController.delete(id)
    return ('Aluno removido com sucesso', 200)