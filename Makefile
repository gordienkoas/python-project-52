build:
	. .venv/bin/activate && ./build.sh
install:
	uv sync

lint:
	ruff check .

migrate:
	uv run python manage.py migrate

test:
	pytest

render-start:
	gunicorn task_manager.wsgi:application

