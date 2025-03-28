from flask import Blueprint, jsonify, request
from app.controllers.professor_controller import ProfessorController

professor_bp = Blueprint('professor', __name__)

@professor_bp.route('/professores', methods=['GET'])
def get_professores():
    professores = ProfessorController.get_all()
    return jsonify([professor.__dict__ for professor in professores])

@professor_bp.route('/professores/<int:id>', methods=['GET'])
def get_professor(id):
    professor = ProfessorController.get_by_id(id)
    return jsonify(professor.__dict__) if professor else ('Professor não encontrado', 404)

@professor_bp.route('/professores', methods=['POST'])
def create_professor():
    data = request.json
    professor = ProfessorController.create(data)
    return jsonify(professor.__dict__), 201

@professor_bp.route('/professores/<int:id>', methods=['PUT'])
def update_professor(id):
    data = request.json
    professor = ProfessorController.update(id, data)
    return jsonify(professor.__dict__)

@professor_bp.route('/professores/<int:id>', methods=['DELETE'])
def delete_professor(id):
    professor = ProfessorController.delete(id)
    return ('Professor removido com sucesso', 200)