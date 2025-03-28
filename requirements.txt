from flask import Flask
from app import create_app

# Inicializa a aplicação Flask utilizando a função create_app
app = create_app()

# Ponto de entrada para rodar o servidor
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)