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
		pytest --cov=src; \
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
