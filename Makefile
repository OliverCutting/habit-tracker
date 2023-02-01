default: help

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: flask
flask: ## Deploy flask site to localhost
	@flask --app main run

.PHONY: setup
setup: ## Install python dependencies
	@pip install -r requirements.txt