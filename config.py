import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    # Configuração de conexão com o banco de dados
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://usuario:12345@localhost/SistemaEscolar')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desativa notificações de modificação no SQLAlchemy
    SECRET_KEY = os.getenv('SECRET_KEY', '123456')  # Chave secreta para segurança