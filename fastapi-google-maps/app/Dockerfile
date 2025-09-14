FROM python:3.12-slim

WORKDIR /app

# Instalar Poetry
RUN pip install --no-cache-dir poetry==1.6.1

# Copiar config de Poetry
COPY pyproject.toml poetry.lock* ./

# Instalar dependencias en contenedor
RUN poetry install --no-root --no-interaction --no-ansi

# Copiar código
COPY app ./app

ENV PYTHONUNBUFFERED=1

# Arrancar FastAPI
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
