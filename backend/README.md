# Shop Scout Backend

FastAPI backend for Shop Scout - a shopping basket price comparison service.

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager

### Setup

```bash
# Install dependencies
make install

# Start development server
make dev
```

**API Available at**: http://localhost:8000
**API Docs**: http://localhost:8000/docs

## 🔧 Development

### Available Commands

```bash
make help           # Show all available commands
make install        # Install dependencies
make dev            # Start development server with hot reload
make test           # Run tests
make test-verbose   # Run tests with verbose output
make test-coverage  # Run tests with coverage report
make lint           # Run linting (ruff, mypy)
make format         # Format code (black, isort, ruff)
make build          # Build for production
```

### Development Workflow

1. **Start development server**:
   ```bash
   make dev
   ```

2. **Run tests** (in another terminal):
   ```bash
   make test
   ```

3. **Check code quality**:
   ```bash
   make lint      # Check for issues
   make format    # Auto-fix formatting
   ```

## 🐳 Docker Development

### Backend-Only Docker

```bash
make docker-up     # Start backend container
make docker-logs   # View logs
make docker-shell  # Access container shell
make docker-down   # Stop container
```

### Manual Docker Commands

```bash
# Build and start
docker-compose build
docker-compose up -d

# View logs
docker-compose logs -f

# Access container
docker-compose exec backend bash

# Stop
docker-compose down
```

## 🧪 Testing

### Running Tests

```bash
make test           # Run all tests
make test-verbose   # Detailed test output
make test-coverage  # Coverage report
```

### Running Specific Tests

```bash
# Test specific file
VIRTUAL_ENV= PYTHONPATH=. uv run pytest src/tests/test_basic.py

# Test specific function
VIRTUAL_ENV= PYTHONPATH=. uv run pytest -k "test_read_index"

# Run with debugging
VIRTUAL_ENV= PYTHONPATH=. uv run pytest -v -s
```

## 📁 Project Structure

```
backend/
├── src/
│   ├── api/              # API routes and endpoints
│   ├── dto/              # Data Transfer Objects
│   ├── tests/            # Test files
│   ├── main.py           # FastAPI application entry point
│   └── static.py         # Static data/configuration
├── Dockerfile            # Docker configuration
├── docker-compose.yaml   # Backend-only Docker setup
├── pyproject.toml        # Python project configuration
├── uv.lock              # Dependency lock file
└── README.md            # This file
```

## 🔍 Code Quality

### Pre-commit Hooks

```bash
make pre-commit-install   # Install hooks
make pre-commit-run       # Run all hooks
```

Pre-commit automatically runs:
- **ruff** - Fast Python linter
- **black** - Code formatter
- **isort** - Import sorter
- **mypy** - Type checker

### Manual Code Quality Checks

```bash
# Check code style and types
make lint

# Auto-fix formatting issues
make format
```

## 🏗️ Building for Production

```bash
# Install production dependencies only
make build

# Or manually
VIRTUAL_ENV= uv sync --no-dev
```

## 🧹 Cleaning Up

```bash
make clean           # Clean Python cache files
make clean-docker    # Clean Docker resources
```

## 📊 API Documentation

Once the server is running, visit:
- **Interactive Docs**: http://localhost:8000/docs (Swagger UI)
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
ENV=development
DEBUG=true
```

### Dependencies

This project uses `uv` for dependency management:

```bash
# Add new dependency
uv add package-name

# Add development dependency
uv add --dev package-name

# Update dependencies
uv sync
```

## 🐛 Troubleshooting

### "Import errors or module not found"

```bash
# Reinstall dependencies
VIRTUAL_ENV= uv sync --dev

# Check virtual environment
VIRTUAL_ENV= uv run python -c "import sys; print(sys.path)"
```

### "Tests not finding modules"

```bash
# Run with correct PYTHONPATH
VIRTUAL_ENV= PYTHONPATH=. uv run pytest
```

### "Docker issues"

```bash
# Clean and rebuild
make clean-docker
make docker-up
```

## 🤝 Contributing

1. **Follow the development workflow**:
   - `make test` - Ensure tests pass
   - `make lint` - Check code quality
   - `make format` - Format code

2. **Write tests** for new features

3. **Update documentation** when needed

4. **Use pre-commit hooks**:
   ```bash
   make pre-commit-install
   ```

---

**For full-stack development**, see the [main README](../README.md).
