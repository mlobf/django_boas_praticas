#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Aplicar migrações
echo "Aplicando migrações..."
python sample_project/manage.py migrate

# Coletar arquivos estáticos (se aplicável)
# echo "Coletando arquivos estáticos..."
# python sample_project/manage.py collectstatic --noinput

# Iniciar o servidor
echo "Iniciando o servidor..."
exec "$@"

