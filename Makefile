build:
	bash -c "source .venv/bin/activate && ./build.sh"

install:
	uv sync

lint:
	ruff check .

migrate:
	uv run python manage.py migrate

start:
	uv run manage.py runserver 0.0.0.0:8000

test:
	pytest

render-start:
	gunicorn task_manager.wsgi:application

