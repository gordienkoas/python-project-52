install:
	uv sync

build:
	./build.sh

migrations:
	uv run python3 manage.py makemigrations

migrate:
	uv run python3 manage.py migrate

collectstatic:
	uv run python3 manage.py collectstatic --no-input

start-server:
	uv run manage.py runserver 0.0.0.0:3000

lint:
	ruff check .

test:
	uv run python3 manage.py test

