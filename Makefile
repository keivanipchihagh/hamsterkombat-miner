# Docker deploy
docker:
	docker-compose up --build -d --no-deps --renew-anon-volumes --force-recreate --remove-orphans
