FROM ghcr.io/astral-sh/uv:python3.11-bookworm

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
WORKDIR /scout_backend

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY src ./src
EXPOSE 8000

CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
