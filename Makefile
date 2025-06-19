install:
	pip install Django

migrate:
	uv run python3 manage.py migrate

collectstatic:
	uv run python3 manage.py collectstatic --no-input

start-server:
	cd code && uv run manage.py runserver 0.0.0.0:3000

test:
	uv run python3 manage.py test

build:
	./build.sh