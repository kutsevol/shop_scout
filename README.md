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
# Clone and start with Docker
git clone <your-repo-url>
cd shop_scout
make docker-up
```

→ **Backend**: http://localhost:8000
→ **API Docs**: http://localhost:8000/docs

### For Developers (Full Setup)

```bash
# Complete development setup
make setup

# Start both backend and frontend
make dev
```

→ **Backend**: http://localhost:8000
→ **Frontend**: http://localhost:5173

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
# Backend API only (always works)
make docker-backend-up

# Full-stack (when frontend Dockerfile is ready)
make docker-up
```

### Docker Workflows

#### **Backend-Only Development**
```bash
make docker-backend-up      # Start API
make docker-backend-logs    # View logs
make docker-backend-down    # Stop API
```

#### **Full-Stack Development**
```bash
make docker-up              # Start everything
make docker-logs            # View all logs
make docker-down            # Stop everything
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

### "Nothing works!"

```bash
# Nuclear option - clean everything and start fresh
make clean-docker
make install
make dev
```

### "Docker is acting weird!"

```bash
# Clean Docker completely
make clean-docker
make docker-up
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
make help           # Show all global commands
make setup          # Complete setup for new developers
make dev            # Start both backend and frontend
make docker-up      # Start full-stack with Docker

# Backend-specific commands
cd backend          # Enter backend directory
make help           # Show backend commands
make test           # Run backend tests
make format         # Format backend code
make docker-up      # Start only backend with Docker

# Or use delegation from root
make backend-help   # Show backend commands from root
make test-backend   # Run backend tests from root
```

---

**Need help?** Run `make help` for global commands or `make backend-help` for backend-specific commands.
