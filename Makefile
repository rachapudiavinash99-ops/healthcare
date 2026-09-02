build:
	docker-compose build
	npm run build --prefix frontend

start:
	docker-compose up -d
	uvicorn backend.app.main:app --reload

test:
	pytest backend/tests/
