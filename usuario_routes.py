from flask import Blueprint, jsonify, request
from app.controllers.usuario_controller import UsuarioController

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = UsuarioController.get_all()
    return jsonify([usuario.__dict__ for usuario in usuarios])

@usuario_bp.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = UsuarioController.get_by_id(id)
    return jsonify(usuario.__dict__) if usuario else ('Usuário não encontrado', 404)

@usuario_bp.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.json
    usuario = UsuarioController.create(data)
    return jsonify(usuario.__dict__), 201

@usuario_bp.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    data = request.json
    usuario = UsuarioController.update(id, data)
    return jsonify(usuario.__dict__)

@usuario_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = UsuarioController.delete(id)
    return ('Usuário removido com sucesso', 200)