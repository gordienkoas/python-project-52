install:
	uv sync

migrate:
	python manage.py migrate

build:
	./build.sh

render-start:
	pip install gunicorn
	gunicorn task_manager.wsgi:application
