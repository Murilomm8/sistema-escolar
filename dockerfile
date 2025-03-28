# Imagem base do MySQL
FROM mysql:latest

# Configurações de variáveis de ambiente para inicialização
ENV MYSQL_ROOT_PASSWORD=12345_root
ENV MYSQL_DATABASE=SistemaEscolar
ENV MYSQL_USER=usuario
ENV MYSQL_PASSWORD=12345

# Copiar o script SQL para o diretório padrão do MySQL no container
COPY sistema_escolar.sql /docker-entrypoint-initdb.d/

# Expor a porta 3306 para acesso ao banco de dados
EXPOSE 3306