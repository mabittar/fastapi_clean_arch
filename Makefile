SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules
PROJECT=fast_clean

# Obtém a tag do último commit
TAG := $(shell git describe --tags --always --abbrev=6)
# Nome da imagem Docker com a tag do último commit
DOCKER_IMAGE_NAME    := ${PROJECT}:${TAG}
LATEST := ${PROJECT}:latest


# Print usage of main targets when user types "make" or "make help"

.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

run: ## Run local app
	( \
		source .venv/bin/activate; \
		clear; \
		echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Runinng APP"; \
		echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		uvicorn src.main:app --reload; \
	)
.PHONY: run


setup: venv requirements.txt
	(\
		clear; \
		echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Start LOCAL environment"; \
		echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Check if virtual environment exists or initiate"; \
		if [ -d ./.venv ]; \
		then \
		echo "virtual environment already exists skip initiation"; \
		else \
		@echo "virtual environment does not exist start creation" \
		python -m venv .venv; \
		fi; \
		clear; \
		echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Start virtual environment"; \
		echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		source .venv/bin/activate; \
		echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Install requirements"; \
		echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		pip install -r requirements.txt; \
		echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Install pre-commit"; \
		echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		pre-commit install; \
	)
.PHONY: setup

tests: ## Run local tests
	( \
		source .venv/bin/activate; \
		clear; \
		echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Runinng tests"; \
		echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		pytest --cov-report term-missing --cov-report html --cov-branch \
           --cov src; \
	)
.PHONY: tests

build: ## Build container based on last commit
	( \
		clear; \
		echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Runinng tests"; \
		echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		docker build -t $(DOCKER_IMAGE_NAME) . ; \
	)
.PHONY: build

compose: ## Start project from docker-compose
	( \
	clear; \
	echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
	echo " Starting containerized environment"; \
	echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
	docker-compose -f docker-compose.yml up -d; \
	)
.PHONY: compose

stop: ## Stop project from docker-compose
	( \
	clear; \
	echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
	echo " Stopping containerized environment"; \
	echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
	docker-compose -f docker-compose.yml stop; \
	)
.PHONY: stop

down: ## Stop project from docker-compose
	( \
	clear; \
	echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
	echo " Down containerized environment"; \
	echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
	docker-compose -f docker-compose.yml down; \
	)
.PHONY: down

lint: ## Lint files and structure using pep8 and sortimports
	( \
		source .venv/bin/activate; \
		clear; \
		echo "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo " Linting APP"; \
		echo "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
        flake8 ./src --count --select=E9,F63,F7,F82 --ignore=U100 --show-source --statistics; \
		black --check -l 120 -t py39 ./src; \
		isort --force-single-line-imports --line-width 120 --skip **/*__init__.py ./src; \
	)
.PHONY: lint

postgres:  ## Deploy local postgress database container
	( \
	clear; \
		echo " ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo "  Deploying Postgres Container"; \
		echo " ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		docker run --name postgresserver -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres; \
		echo "Postgres container deployed. Set envVar to: postgresql://postgres:postgres@localhost/app"; \

	)
.PHONY: postgres

postgres_stop:  ## Stop local postgres database container
	( \
	clear; \
		echo " ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		echo "  Stopping Postgres Container"; \
		echo " ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; \
		docker stop postgresserver || true && docker rm postgresserver || true \
		echo "Postgres container stopped."; \

	)
.PHONY: postgres_stop

clean: ## Remove unecessary files and folder
	(\
	clear; \
	find . -type f -name '*.py[co]' -delete; \
	find . -type d -name '__pycache__' -delete; \
	rm -rf dist; \
	rm -rf build; \
	rm -rf *.egg-info; \
	rm -rf .hypothesis; \
	rm -rf .pytest_cache; \
	rm -rf .tox; \
	rm -f report.xml; \
	rm -f coverage.xml; \
	rm -rf coverage_html_report; \
	)
.PHONY: clean
