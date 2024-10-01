#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Aplicar migrações
echo "Aplicando migrações..."
echo "Aplicando make migrations..."
python3 sample_project/manage.py makemigrations
echo "Aplicando make migrate..."
python3 sample_project/manage.py migrate

# Criar superusuário se não existir
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
    echo "Verificando se o superusuário existe..."
    python3 sample_project/manage.py createsuperuser \
        --username "$DJANGO_SUPERUSER_USERNAME" \
        --email "$DJANGO_SUPERUSER_EMAIL" \
        --noinput || true
    echo "Superusuário verificado ou criado."
fi

# Iniciar o servidor
echo "Iniciando o servidor..."
exec "$@"



