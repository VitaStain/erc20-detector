.PHONY: help test watch build up down deploy restart
include .env

all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

help: # Show help for each of the Makefile recipes.
	@grep -E "^[a-zA-Z0-9 -]+:.*#"  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

watch: # Watch docker containers
	docker compose --project-directory . watch

build: # Build docker images
	docker compose --project-directory . build

up: # Start docker containers
	docker compose --project-directory . up -d

down: # Stop docker containers
	docker compose --project-directory . down --remove-orphans

logs: # Follow logs
	docker logs -f $(CONTAINER_NAME)

deploy: down up # Down and up docker containers
restart: down up # Down and up docker containers
