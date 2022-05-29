build-and-run: build run

run:
	docker compose run main

build:
	docker compose build

push:
	docker compose push
