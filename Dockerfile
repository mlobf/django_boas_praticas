# Use uma imagem oficial do Python como base
FROM python:3.12-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo de dependências para o contêiner
COPY requirements.txt ./

# Instale as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código para o contêiner
COPY . .

# Ajuste as permissões do script de entrada
RUN chmod +x /app/entrypoint.sh

# Defina o script de entrada
ENTRYPOINT ["/app/entrypoint.sh"]

# Exponha a porta 8000
EXPOSE 8000

# Comando para rodar o servidor de desenvolvimento do Django
CMD ["python", "sample_project/manage.py", "runserver", "0.0.0.0:8000"]

