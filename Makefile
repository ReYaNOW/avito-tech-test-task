PORT ?= 8080


install:
	poetry install --no-root
	make migrate

start:
	poetry run uvicorn stats_counter.main:app --host 0.0.0.0 --port $(PORT) --reload

sql_migrations:
	poetry run alembic revision --autogenerate

migrate:
	poetry run alembic upgrade head

compose-setup:
	docker compose build
	make compose-migrate

compose-start:
	docker compose up --abort-on-container-exit || true

compose-migrations:
	docker compose run --rm web make sql_migrations

compose-migrate:
	docker compose run --rm web alembic upgrade head

enter-db:
	docker compose up --abort-on-container-exit --no-start
	docker compose start db
	docker compose exec -it db psql -U pguser -d pgdb psql

compose-stop:
	docker compose stop || true

compose-down:
	docker compose down --remove-orphans || true
