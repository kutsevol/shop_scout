# Backend Makefile
# =================

.PHONY: help install dev test lint format build docker-build docker-up docker-down docker-logs clean

# Default target
help: ## Show backend commands
	@echo "Backend - Available commands:"
	@echo ""
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# Installation
install: ## Install backend dependencies
	@echo "Installing backend dependencies..."
	VIRTUAL_ENV= uv sync --all-groups --all-extras

# Development
dev: ## Start backend development server
	@echo "Starting backend development server..."
	VIRTUAL_ENV= uv run python src/main.py

# Testing
test: ## Run backend tests
	@echo "Running backend tests..."
	VIRTUAL_ENV= PYTHONPATH=. uv run pytest


# Code Quality
lint: ## Run backend linting (ruff, mypy)
	@echo "Running backend linting..."
	VIRTUAL_ENV= uv run ruff check src/
	VIRTUAL_ENV= uv run mypy src/

format: ## Format backend code (black, isort, ruff)
	@echo "Formatting backend code..."
	VIRTUAL_ENV= uv run black src/
	VIRTUAL_ENV= uv run isort src/
	VIRTUAL_ENV= uv run ruff check --fix src/

# Pre-commit
pre-commit-install: ## Install pre-commit hooks
	@echo "Installing pre-commit hooks..."
	VIRTUAL_ENV= uv run pre-commit install

pre-commit-run: ## Run pre-commit on all files
	@echo "Running pre-commit on all files..."
	VIRTUAL_ENV= uv run pre-commit run --all-files --config ../.pre-commit-config.yaml

# Build
build: ## Build backend (install production dependencies)
	@echo "Building backend..."
	VIRTUAL_ENV= uv sync --no-dev

# Docker
docker-build: ## Build backend Docker container
	@echo "Building backend Docker container..."
	docker-compose -f docker-compose.dev.yaml build

docker-up: ## Start backend Docker container
	@echo "Starting backend Docker container..."
	docker-compose up -d

docker-down: ## Stop backend Docker container
	@echo "Stopping backend Docker container..."
	docker-compose down

docker-logs: ## Show backend Docker logs
	@echo "Showing backend Docker logs..."
	docker-compose logs -f

docker-restart: docker-down docker-up ## Restart backend Docker container

docker-shell: ## Access running backend container shell
	@echo "Accessing backend container shell..."
	docker-compose exec backend bash

# Cleanup
clean: ## Clean backend build artifacts
	@echo "Cleaning backend..."
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.pyc" -delete
	rm -rf .mypy_cache .ruff_cache .pytest_cache dist build *.egg-info

clean-docker: ## Clean backend Docker resources
	@echo "Cleaning backend Docker resources..."
	docker-compose down --volumes --remove-orphans

# Shortcuts
run: dev ## Alias for dev
start: docker-up ## Alias for docker-up
stop: docker-down ## Alias for docker-down
