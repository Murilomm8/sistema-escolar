from flask import Blueprint, jsonify, request
from app.controllers.atividade_aluno_controller import AtividadeAlunoController

atividade_aluno_bp = Blueprint('atividade_aluno', __name__)

@atividade_aluno_bp.route('/atividade_alunos', methods=['GET'])
def get_atividade_alunos():
    atividades_alunos = AtividadeAlunoController.get_all()
    return jsonify([atividade_aluno.__dict__ for atividade_aluno in atividades_alunos])

@atividade_aluno_bp.route('/atividade_alunos/<int:id_atividade>/<int:id_aluno>', methods=['GET'])
def get_atividade_aluno(id_atividade, id_aluno):
    atividade_aluno = AtividadeAlunoController.get_by_id(id_atividade, id_aluno)
    return jsonify(atividade_aluno.__dict__) if atividade_aluno else ('Relação não encontrada', 404)

@atividade_aluno_bp.route('/atividade_alunos', methods=['POST'])
def create_atividade_aluno():
    data = request.json
    atividade_aluno = AtividadeAlunoController.create(data)
    return jsonify(atividade_aluno.__dict__), 201

@atividade_aluno_bp.route('/atividade_alunos/<int:id_atividade>/<int:id_aluno>', methods