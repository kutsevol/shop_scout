# Shop Scout Global Makefile
# ===========================
# Coordinates full-stack development and delegates to component Makefiles

.PHONY: help install dev test lint format build clean setup health backend-help
.PHONY: install-backend install-frontend dev-backend dev-frontend test-backend lint-backend lint-frontend
.PHONY: build-backend build-frontend clean-backend clean-frontend clean-docker
.PHONY: docker-backend-build docker-backend-up docker-backend-down docker-backend-logs docker-backend-restart
.PHONY: pre-commit-install pre-commit-run run
.PHONY: prod-build prod-up prod-down prod-restart prod-logs prod-ps prod-health prod-start prod-stop

# ===== General =====
help: ## Show global commands
	@echo "\033[1mShop Scout - Global Commands:\033[0m"
	@echo ""
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_.-]+:.*?## / {printf "  \033[36m%-25s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
	@echo "\033[1mComponent-specific commands:\033[0m"
	@echo "  \033[33mmake backend-help\033[0m       Show backend-specific commands"
	@echo "  \033[33mcd backend && make help\033[0m Direct backend commands"

backend-help: ## Show backend make help
	@$(MAKE) -C backend help

# ===== Install =====
install: install-backend install-frontend ## Install all dependencies (backend + frontend)

install-backend: ## Install backend dependencies
	@echo "Installing backend dependencies..."
	$(MAKE) -C backend install

install-frontend: ## Install frontend dependencies
	@echo "Installing frontend dependencies..."
	cd frontend && npm install

# ===== Development =====
dev: ## Start both backend and frontend development servers
	@echo "Starting full-stack development servers..."
	@echo "Backend: http://localhost:8000 | Frontend: http://localhost:5173"
	@$(MAKE) -j2 dev-backend dev-frontend

dev-backend: ## Start only backend development server
	@echo "Starting backend development server..."
	$(MAKE) -C backend dev

dev-frontend: ## Start only frontend development server
	@echo "Starting frontend development server..."
	cd frontend && npm run dev

# ===== Testing =====
test: ## Run all tests
	@echo "Running all tests..."
	$(MAKE) -C backend test
	# Add frontend tests here when available

test-backend: ## Run backend tests only
	@echo "Running backend tests..."
	$(MAKE) -C backend test

# ===== Code Quality =====
lint: lint-backend lint-frontend ## Run linting for both backend and frontend

lint-backend: ## Run backend linting
	@echo "Running backend linting..."
	$(MAKE) -C backend lint

lint-frontend: ## Run frontend linting
	@echo "Running frontend linting..."
	cd frontend && npm run lint

format: ## Format code (currently backend only)
	@echo "Formatting code..."
	$(MAKE) -C backend format

# ===== Pre-commit =====
pre-commit-install: ## Install pre-commit hooks
	@echo "Installing pre-commit hooks..."
	$(MAKE) -C backend pre-commit-install

pre-commit-run: ## Run pre-commit on all files
	@echo "Running pre-commit checks..."
	$(MAKE) -C backend pre-commit-run

# ===== Build (app artifacts) =====
build: build-backend build-frontend ## Build both backend and frontend
build-backend: ## Build backend for production
	@echo "Building backend..."
	$(MAKE) -C backend build
build-frontend: ## Build frontend for production
	@echo "Building frontend..."
	cd frontend && npm run build

# ===== Docker Development =====
# NOTE: Full-stack docker-compose.yaml not yet implemented
# Use individual backend commands or make dev for development

# Uncomment these when full-stack Docker is implemented:
# docker-build: ## Build full-stack Docker containers
# 	@echo "Building full-stack Docker containers..."
# 	docker compose build
#
# docker-up: ## Start full-stack Docker containers
# 	@echo "Starting full-stack Docker containers..."
# 	docker compose up -d
#
# docker-down: ## Stop full-stack Docker containers
# 	@echo "Stopping full-stack Docker containers..."
# 	docker compose down
#
# docker-logs: ## Show full-stack Docker logs
# 	@echo "Showing full-stack Docker logs..."
# 	docker compose logs -f
#
# docker-restart: docker-down docker-up ## Restart full-stack Docker containers

# Backend-only Docker targets (use these for now)
docker-backend-build: ## Build backend Docker container
	@echo "Building backend Docker container..."
	$(MAKE) -C backend docker-build

docker-backend-up: ## Start backend Docker container
	@echo "Starting backend Docker container..."
	@echo "Backend: http://localhost:8000"
	$(MAKE) -C backend docker-up

docker-backend-down: ## Stop backend Docker container
	@echo "Stopping backend Docker container..."
	$(MAKE) -C backend docker-down

docker-backend-logs: ## Show backend Docker logs
	@echo "Showing backend Docker logs..."
	$(MAKE) -C backend docker-logs

docker-backend-restart: docker-backend-down docker-backend-up ## Restart backend Docker container

clean-docker: ## Clean Docker resources
	@echo "Cleaning Docker resources..."
	$(MAKE) -C backend clean-docker

# ===== Cleanup =====
clean: clean-backend clean-frontend ## Clean all build artifacts
clean-backend: ## Clean backend build artifacts
	@echo "Cleaning backend..."
	$(MAKE) -C backend clean
clean-frontend: ## Clean frontend build artifacts
	@echo "Cleaning frontend..."
	cd frontend && rm -rf node_modules dist .vite

# ===== Setup for new developers =====
setup: install pre-commit-install ## Complete setup for new developers
	@echo ""
	@echo "\033[1;32m✅ Setup completed!\033[0m"
	@echo ""
	@echo "\033[1mNext steps:\033[0m"
	@echo "  \033[36mmake dev\033[0m          Start development servers"
	@echo "  \033[36mmake docker-up\033[0m    Start with Docker (full-stack)"
	@echo "  \033[36mmake help\033[0m         Show all commands"
	@echo ""

# ===== Health (local/dev) =====
health: ## Check if services are running (local/dev)
	@echo "Checking service health..."
	@curl -s http://localhost:8000/ > /dev/null && echo "✅ Backend: http://localhost:8000" || echo "❌ Backend not running"
	@curl -s http://localhost:5173/ > /dev/null && echo "✅ Frontend: http://localhost:5173" || echo "❌ Frontend not running"

# ===== Production (server) =====
# Use a dedicated compose file in repo root
PROD_COMPOSE := -f docker-compose.prod.yaml
SHOP_SCOUT_URL ?= http://your-domain.com/shop_scout

prod-build: ## Build prod images (backend only)
	@echo "Building prod backend image..."
	docker compose $(PROD_COMPOSE) build

prod-up: ## Start prod stack (backend behind Caddy)
	@echo "Starting prod backend..."
	docker compose $(PROD_COMPOSE) up -d --build --force-recreate

prod-down: ## Stop prod stack
	@echo "Stopping prod backend..."
	docker compose $(PROD_COMPOSE) down --remove-orphans

prod-restart: prod-down prod-up ## Restart prod stack

prod-logs: ## Tail prod backend logs
	docker compose $(PROD_COMPOSE) logs -f backend

prod-ps: ## Show prod containers
	docker compose $(PROD_COMPOSE) ps

prod-health: ## Check prod health via Caddy
	@echo "Checking: $(SHOP_SCOUT_URL)/"
	@curl -fsS "$(SHOP_SCOUT_URL)/" >/dev/null && echo "✅ Up" || (echo "❌ Down" && exit 1)

# Shortcuts (Development)
run: dev ## Alias for dev (start native development servers)
# NOTE: start/stop shortcuts disabled until full-stack Docker is implemented
# start: docker-up ## Alias for docker-up (start full-stack containers) - NOT IMPLEMENTED
# stop: docker-down ## Alias for docker-down (stop full-stack containers) - NOT IMPLEMENTED

# Shortcuts (Production)
prod-start: prod-up ## Alias for prod-up
prod-stop: prod-down ## Alias for prod-down
