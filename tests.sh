#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Nome do serviço Django conforme definido no docker-compose.yml
SERVICE_NAME="web"

# Inicia os contêineres em segundo plano
echo "Iniciando os contêineres Docker..."
docker-compose up -d

# Função para verificar se o PostgreSQL está pronto
wait_for_db() {
    echo "Aguardando o PostgreSQL estar pronto..."
    while ! docker-compose exec db pg_isready -U myuser > /dev/null 2>&1; do
        echo "PostgreSQL não está pronto ainda. Aguardando..."
        sleep 1
    done
    echo "PostgreSQL está pronto!"
}

# Chama a função para esperar o banco de dados
wait_for_db

# Executa os testes do Django no diretório correto
echo "Executando os testes do Django..."
docker-compose exec -w /app/sample_project $SERVICE_NAME python3 manage.py test main --verbosity=2

# Opcional: Para os contêineres após os testes
# echo "Parando os contêineres Docker..."
# docker-compose down

echo "Testes concluídos com sucesso!"

