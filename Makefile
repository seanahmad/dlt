#!make
PROJECT_VERSION := 0.2.1

SHELL := /bin/bash
IMAGE := tschm/dlt


.PHONY: help build jupyter tag


.DEFAULT: help

help:
	@echo "make build"
	@echo "       Build the docker image."
	@echo "make jupyter"
	@echo "       Start the Jupyter server."
	@echo "make tag"
	@echo "       Make a tag on Github."


build:
	docker-compose build jupyter

jupyter: build
	echo "http://localhost:${PORT}"
	docker-compose up jupyter

tag:
	git tag -a ${PROJECT_VERSION} -m "new tag"
	git push --tags
