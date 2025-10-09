# Shop Scout

> Compare and optimize your shopping basket costs across multiple stores, cities, and countries.

## 🎯 What is Shop Scout?

Shop Scout is a full-stack application that helps users:
- **Compare prices** across different stores and locations
- **Optimize shopping baskets** for the best deals
- **Track price changes** over time
- **Find alternatives** for expensive items

## 🚀 Quick Start

### For Users (Just Run the App)

```bash
# Clone and setup
git clone <your-repo-url>
cd shop_scout
make setup

# If make dev fails, try individual components:
make dev-backend    # In one terminal
make dev-frontend   # In another terminal
```

→ **Backend**: http://localhost:8000
→ **Frontend**: http://localhost:5173 (or next available port)
→ **API Docs**: http://localhost:8000/docs

### For Developers (Full Setup)

```bash
# Complete development setup
make setup

# Start both backend and frontend
make dev
```

→ **Backend**: http://localhost:8000
→ **Frontend**: http://localhost:5173 (or 5174 if 5173 is busy)

⚠️ **Note**: `make dev` may fail due to configuration issues. See [Troubleshooting](#-troubleshooting) if you get errors.

## 💻 Development Workflows

### 🌅 Daily Development Flow

```bash
# 1. Start your day
git pull
make dev                    # Start both services

# 2. Make changes and test
make test                   # Run tests

# 3. Before committing
make lint                   # Check code quality
make pre-commit-run         # Final validation

# 4. Commit changes
git add . && git commit -m "Your changes"
```

### 🎨 Frontend Development

```bash
# Frontend-focused development
make dev-frontend           # Start only frontend

# The backend team provides:
# - API endpoints at http://localhost:8000
# - Interactive docs at http://localhost:8000/docs
# - Docker setup for consistent API
```

### 🔧 Backend Development

```bash
# Backend-focused development
cd backend
make dev                    # Backend development server
make test                   # Backend tests
make format                 # Code formatting
```

See [backend README](backend/README.md) for detailed backend development.

## 🐳 Docker Development

### Quick Docker Start

```bash
# Backend API only (currently available)
make docker-backend-up

# Full-stack Docker setup is not yet implemented
# Use: make dev (for development with separate processes)
```

### Docker Workflows

#### **Backend-Only Development** (Available)
```bash
make docker-backend-up      # Start API
make docker-backend-logs    # View logs
make docker-backend-down    # Stop API
```

#### **Full-Stack Development** (Not Yet Available)
❌ **Note**: Full-stack Docker setup (`docker-compose.yaml`) is not yet implemented.

For now, use separate development servers:
```bash
make dev                    # Start both backend and frontend (separate processes)
# OR
make dev-backend            # Backend: http://localhost:8000
make dev-frontend           # Frontend: http://localhost:5173
```

## 🚀 Production Deployment

### Production Commands

```bash
# Build production images
make prod-build             # Build backend for production

# Start/stop production stack
make prod-up                # Start production backend (behind Caddy)
make prod-down              # Stop production backend
make prod-restart           # Restart production stack

# Monitor production
make prod-logs              # View production logs
make prod-ps                # Show production containers status
make prod-health            # Check production health
```

### Production Environment

The production setup uses a separate Docker Compose file (`docker-compose.prod.yaml`) and runs the backend behind Caddy reverse proxy.

**Environment Variables:**
- `SHOP_SCOUT_URL` - Production URL (default: `http://91.238.105.236/shop_scout`)

**Production Health Check:**
```bash
# Check if production is running
make prod-health

# Or manually
curl -fsS "http://91.238.105.236/shop_scout/" && echo "✅ Up" || echo "❌ Down"
```

## ⚡ Quick Shortcuts

For convenience, some commonly used commands have shorter aliases:

```bash
# Development shortcuts
make run                    # Same as: make dev

# Docker shortcuts (NOT WORKING - no docker-compose.yaml)
# make start                # Would be: make docker-up (❌ not implemented)
# make stop                 # Would be: make docker-down (❌ not implemented)
```


## 🏗️ Project Architecture

### Technology Stack

**Backend** (`/backend/`):
- **FastAPI** - Modern Python web framework
- **uv** - Fast Python package manager
- **Docker** - Containerized development and deployment
- **pytest** - Testing framework
- **ruff/black/mypy** - Code quality tools

**Frontend** (`/frontend/`):
- **React** - UI library
- **Vite** - Build tool and development server
- **TypeScript** - Type-safe JavaScript
- **Material-UI** - Component library

### Component Communication

```
┌───────────┐       ┌───────────┐
│ Frontend  │ HTTP  │ Backend   │
│ React     │ ←────→ │ FastAPI   │
│ :5173     │       │ :8000     │
└───────────┘       └───────────┘
```


## 🔧 Troubleshooting

### "make dev fails immediately!"

**Backend Error: `Extra inputs are not permitted [forwarded_allow_ips]`**
```bash
# Fix: Remove problematic env variable or update config
echo "# FORWARDED_ALLOW_IPS=127.0.0.1,::1" > .env  # Comment it out
# OR
cd backend && make dev  # Start backend separately to debug
```

**Frontend Port Conflict: `Port 5173 is in use`**
```bash
# Kill existing frontend process
lsof -ti:5173 | xargs kill -9
# OR let it use the next available port (5174)
```

### "Nothing works!"

```bash
# Nuclear option - clean everything and start fresh
make clean-docker
make install
# Fix backend config first, then:
make dev
```

### "Docker is acting weird!"

```bash
# Clean Docker completely
make clean-docker
# Then start backend-only Docker:
make docker-backend-up
# OR use development servers (after fixing config):
make dev
```

### "Tests are failing!"

```bash
# Reinstall dependencies and try again
make install-backend
make test
```

### "I'm getting import errors!"

This usually means the Python environment isn't set up correctly. The project uses `uv` for dependency management:

```bash
cd backend
VIRTUAL_ENV= uv sync --dev  # Reinstall dependencies
```

## 🎯 What Each Component Does

- **Backend** (`/backend`): FastAPI application that provides the API
- **Frontend** (`/frontend`): React application for the user interface
- **Docker**: Containerized backend (frontend runs in development mode only)
- **Makefile**: Convenient commands for common tasks
- **Pre-commit**: Automatic code quality checks

## 📚 API Documentation

Once the backend is running, visit http://localhost:8000/docs for interactive API documentation.

## 🤝 Contributing

1. Make sure `make test` passes
2. Make sure `make lint` passes
3. Run `make pre-commit-run` before committing
4. Write tests for new features
5. Update documentation if needed

## 🔧 Makefile Structure

This project uses **two Makefiles** for better organization:

### **Global Makefile** (root directory)
- **Purpose**: Coordinates full-stack development
- **Usage**: `make <command>` from project root
- **Focus**: Installation, full-stack development, Docker orchestration

### **Backend Makefile** (`backend/Makefile`)
- **Purpose**: Backend-specific operations
- **Usage**: `cd backend && make <command>`
- **Focus**: Backend testing, linting, formatting, backend-only Docker

### **Quick Reference**
```bash
# Global commands (from root)
make help               # Show all global commands
make setup              # Complete setup for new developers
make dev                # Start both backend and frontend (separate processes)
# make docker-up        # ❌ Not implemented (no docker-compose.yaml)
# make docker-down      # ❌ Not implemented
# make docker-logs      # ❌ Not implemented

# Shortcuts (aliases)
make run                # Alias for: make dev
# make start            # Alias for: make docker-up (❌ not implemented)
# make stop             # Alias for: make docker-down (❌ not implemented)

# Backend-specific commands
cd backend              # Enter backend directory
make help               # Show backend commands
make test               # Run backend tests
make format             # Format backend code
make docker-up          # Start only backend with Docker

# Or use delegation from root
make backend-help       # Show backend commands from root
make test-backend       # Run backend tests from root

# Production (server)
make prod-build         # Build prod backend image
make prod-up            # Start prod backend (Caddy proxy)
make prod-down          # Stop prod backend
make prod-restart       # Restart prod backend
make prod-logs          # Tail prod backend logs
make prod-ps            # Show prod containers
make prod-health        # Check prod health (uses SHOP_SCOUT_URL)
```

Note: Production commands use docker-compose.prod.yaml and respect SHOP_SCOUT_URL (default: http://your-domain/shop_scout).

---

**Need help?** Run `make help` for global commands or `make backend-help` for backend-specific commands.
