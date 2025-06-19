install:
	uv sync

migrate:
	uv run python3 manage.py migrate

start-server:
	uv run manage.py runserver 0.0.0.0:8000

test:
	uv run python3 manage.py test

build:
	./build.sh