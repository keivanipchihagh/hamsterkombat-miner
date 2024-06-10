# Docker deploy
docker:
	docker-compose -p $(name) up --build -d
