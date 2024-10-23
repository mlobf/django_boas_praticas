# Makefile

# Declaração de alvos que não são arquivos
.PHONY: up test down help

# Alvo padrão para exibir ajuda
help:
	@echo "Comandos disponíveis:"
	@echo "  make up     		- Inicia os contêineres Docker em segundo plano"
	@echo "  make run    		- Executa o bash dentro do container"
	@echo "  make test   		- Executa os testes usando o script tests.sh"
	@echo "  make down   		- Para e remove os contêineres Docker"
	@echo "  make help   		- Exibe esta mensagem de ajuda"
	@echo "  make shell_plus   	- Exibe esta mensagem de ajuda"

# Alvo para iniciar os contêineres Docker
up:
	docker-compose up --build

# Alvo para entrar dentro do container no modo interativo
run:
	docker-compose up --build -d
	docker exec -it django_boas_praticas-web-1 /bin/bash

# Alvo para executar os testes
test:
	./tests.sh

# Alvo para parar os contêineres Docker
down:
	docker-compose down

# Alvo para executar o shell_plus
shell_plus:
	docker-compose up --build -d
	docker-compose exec web python sample_project/manage.py shell_plus




