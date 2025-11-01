# ============================
# 🏗️ Stage 1 — Build dependencies
# ============================
FROM python:3.13-slim AS builder

# Prevent Python from writing .pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies for building
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy only dependency files first (for layer caching)
COPY pyproject.toml poetry.lock* ./

# Install dependencies (no dev dependencies)
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --only main

# Copy application source
COPY . .

# ============================
# 🚀 Stage 2 — Runtime
# ============================
FROM python:3.13-slim AS runtime

# Set working directory
WORKDIR /app

# Copy Poetry-installed environment from builder
COPY --from=builder /usr/local/lib/python3.13 /usr/local/lib/python3.13
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app /app

# Expose FastAPI default port
EXPOSE 8000

# Default command — start FastAPI with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


# Remeber to use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them