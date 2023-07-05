build-image:
	docker image build -t python-telegrambot-docker --network=host .

run-image:
	docker run --network=host --restart=always --memory 512m --memory-swap 768m --cpus=".5" -p 7000:7000 --env-file ./.env python-telegrambot-docker

up-dev:
	docker-compose up --build

up-prod:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build

down:
	docker-compose down