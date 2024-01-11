SHELL := /bin/bash

include .env

.PHONY: poetry
poetry:
	@pipx --version > /dev/null 2>&1 || (echo "pipx is required, installing now..." && sudo apt -y install pipx)
	@poetry --version > /dev/null 2>&1 || (echo "poetry is required, installing now..." && pipx install poetry)
	poetry env use python3

.PHONY: clean
clean: poetry
	rm -rf .venv && poetry env remove --all

.PHONY: install 
install: poetry
	poetry update install

.PHONY: build
build: poetry install
	poetry run python -m grpc_tools.protoc -Iserver/time=./protos --python_out=./src --grpc_python_out=./src ./protos/time.proto

.PHONY: test
test: poetry
	poetry update install --with test
	poetry run black src tests
	poetry run pytest -v

.PHONY: run
run: build
	export PYTHONPATH=$(shell pwd)/src && \
	poetry run python src/main.py
