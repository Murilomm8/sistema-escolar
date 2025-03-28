from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes import register_routes

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    register_routes(app)  # Registra todas as rotas

    with app.app_context():
        db.create_all()  # Cria as tabelas automaticamente

    return app

    from app.routes.aluno_routes import aluno_bp

def register_routes(app):
    app.register_blueprint(aluno_bp, url_prefix='/api')