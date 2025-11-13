FROM python:3.13-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock* /app/

RUN pip install --no-cache-dir poetry

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root --only main

# Установка gunicorn, если не включён в зависимости
RUN pip install gunicorn

COPY . /app/

RUN mkdir -p /app/media /app/static

ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=config.settings

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
