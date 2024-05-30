install:
	pip install poetry
	poetry install

start:
	poetry run python icecream_api/app.py

update:
	poetry update

lint:
	poetry run flake8
