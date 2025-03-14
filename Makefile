SHELL=/bin/bash
.DEFAULT_GOAL := default

.PHONY: venv
venv:
	@echo "---------------------------"
	@echo "- Activating poetry shell -"
	@echo "---------------------------"
	poetry shell

.PHONY: install
install:
	@echo "---------------------------"
	@echo "- Installing dependencies -"
	@echo "---------------------------"
	poetry shell
	poetry install
	pre-commit install

.PHONY: update
update:
	@echo "-------------------------"
	@echo "- Updating dependencies -"
	@echo "-------------------------"
	poetry shell
	poetry update

.PHONY: lint
lint:
	@echo "-----------------------------"
	@echo "- Run linters and formatters -"
	@echo "-----------------------------"
	SKIP=no-commit-to-branch pre-commit run --all-files

.PHONY: pull
pull:
	@echo "------------------------"
	@echo "- Pulling last changes -"
	@echo "------------------------"
	git checkout master
	git pull

.PHONY: run
run:
	@echo "----------------------"
	@echo "- Running API server -"
	@echo "----------------------"
	uvicorn app.travelai.src.api.main:api --reload --log-level debug
