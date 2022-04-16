CURRENT_DIRECTORY := $(shell pwd)
TESTSCOPE = apps
TESTFLAGS = --with-timer --timer-top-n 10 --keepdb


help:
	@echo "Docker Compose Help"
	@echo "-----------------------"
	@echo ""
	@echo "Run tests to ensure current state is good:"
	@echo "    make test"
	@echo ""
	@echo "If tests pass, add fixture data and start up the api:"
	@echo "    make begin"
	@echo ""
	@echo "Really, really start over:"
	@echo "    make clean"
	@echo ""
	@echo "See contents of Makefile for more targets."
.PHONY: help

install-dependencies:
	pip install -r requirements.txt
.PHONY: install-dependencies

collectstatic:
	python manage.py collectstatic --no-input
.PHONY: collectstatic

server:
	python manage.py runserver 0.0.0.0:8000
.PHONY: server

dev-setup: \
	install-dependencies \
	make-migration \
	migrate \
	collectstatic
.PHONY: dev-setup

local-ci: \
	checks \
	isort \
	flake8 \
	autopep8
.PHONY: local-ci

apply-isort:
	isort .
.PHONY: apply-isort

isort:
	isort -c --df .
.PHONY: isort

checks:
	python manage.py check
.PHONY: checks

make-migration:
	python manage.py makemigrations --no-input
.PHONY: makemigrations

migrate:
	python manage.py migrate --no-input
.PHONY: migrate

autopep8:
	autopep8 -d .
.PHONY: autopep8

flake8:
	flake8 -v --count --show-source --statistics
.PHONY: flake8

private-settings:
	echo 'SECRET_KEY="$(SECRET_KEY)"' > $$(pwd)/base/settings/.env
	echo 'ALLOWED_HOSTS="$(ALLOWED_HOSTS)"' >> $$(pwd)/base/settings/.env
	echo 'ENV_NAME="$(ENV_NAME)"' >> $$(pwd)/base/settings/.env
.PHONY: private-settings