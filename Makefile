# Makefile

# Declaração de alvos que não são arquivos
.PHONY: up test down help

# Alvo padrão para exibir ajuda
help:
	@echo "Comandos disponíveis:"
	@echo "  make up     - Inicia os contêineres Docker em segundo plano"
	@echo "  make test   - Executa os testes usando o script tests.sh"
	@echo "  make down   - Para e remove os contêineres Docker"
	@echo "  make help   - Exibe esta mensagem de ajuda"

# Alvo para iniciar os contêineres Docker
up:
	docker-compose up --build

# Alvo para executar os testes
test:
	./tests.sh

# Alvo para parar os contêineres Docker
down:
	docker-compose down

