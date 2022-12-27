ENV=development
PROJECT=app
TEST_FILES=./tests
LINTING_PYTHON_FILES=app/**/*.py
LINTING_TEST_FILES=tests/**/*.py

GIT_FILES=$$(git diff --name-only | grep .py)

FLAKE8_FLAGS = --ignore=W503,E501
ISORT_FLAGS = --profile=black --lines-after-import=2


.PHONY: all help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

## @ Environment
.PHONY: clean
clean: ## Remove cache files from project
	@echo "cleaning cache files"
	@py3clean .
	@rm -rf .cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov coverage-report
	@rm -rf .tox/
	@rm -rf docs/_build
	@rm -rf docs/_build
	@echo "Done!"

## @ Application
.PHONY: test run migrate upgrade sql_upgrade
test: ## Run tests and save coverage
	python -m pytest -vv -p no:warnings \
		${TEST_FILES} \
		--cov=app \
		--cov-report=term \
		--cov-report=html:coverage-report \
		--no-cov-on-fail \
		--disable-pytest-warnings

run: ## Executa aplicação localmente
	@uvicorn app.main:app --reload

makemigrations: ## Cria as migrações do Alembic
	@alembic revision --autogenerate

upgrade: ## Aplica as migrações do Alembic
	@alembic upgrade head

sql_upgrade: ## Gera o SQL das migrações do Alembic
	@alembic upgrade head --sql > sql_upgrade.sql

## @ Sintax checking
.PHONY: lint lint_black lint_isort flake bandit

flake:
	@echo "Checking Flake..."
	@flake8 ${FLAKE8_FLAGS} .
	@echo "Done!"
lint_isort:
	@echo "Checking ISort..."
	@isort ${ISORT_FLAGS} --check ${PROJECT}/**/*.py
	@echo "Done!"
bandit:
	@echo "Checking Bandit..."
	@bandit -r -l --ignore-nosec ${PROJECT}
	@echo "Done!"
lint_black:
	@echo "Checking Black..."
	@black -l 140 --check ${PROJECT}/**/*.py
	@black -l 140 --check tests/**/*.py
lint: flake lint_isort lint_black bandit   ## Roda analise estatica: black, flake, isort e bandit

## @ Formatação
.PHONY: format_project format_test format
format_project:
	black -l 140 ${LINTING_PYTHON_FILES}
	isort ${LINTING_PYTHON_FILES}
format_test:
	black -l 140 ${LINTING_TEST_FILES}
	isort ${LINTING_TEST_FILES}
format_git:  ## Formata os arquivos alterados com black e isort
	@black -l 140 ${GIT_FILES}
	@isort ${ISORT_FLAGS} ${GIT_FILES}
format: format_project format_test ## Formata o código com black e isort
