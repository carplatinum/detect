# Detect Project
## Описание
Detect — это backend проект на Django для перевода слов с изображений без изменения изображения, с заменой текста прямо на самом изображении. Используется OCR для распознавания текста, перевод через API, а результат накладывается поверх изображения.
Проект включает REST API с JWT аутентификацией, Celery для фоновых задач, Docker-контейнеры и конфигурацию для CI/CD.

# Особенности
Загрузка и обработка изображений через API

Асинхронный OCR и перевод текста с использованием Celery и Redis

Перевод текста на изображении с наложением оригинального расположения слов

Аутентификация и управление пользователями (JWT, DRF)

Контейнеризация с Docker и оркестрация с docker-compose

Полный CI/CD pipeline с GitHub Actions для тестирования, сборки и деплоя

Nginx как обратный прокси и сервер статических файлов

# Используемые технологии
Python 3.13, Django 5.x

Django REST Framework (DRF)

Celery + Redis для фоновых задач и планировщика periodic tasks

PostgreSQL как основная база данных

Gunicorn сервер

Docker + Docker Compose

Nginx (обратный прокси + статические файлы)

Poetry для управления зависимостями

Pytest для тестов, Flake8 для линтинга

GitHub Actions для автоматизации CI/CD

Яндекс.Облако (Yandex Cloud) — платформа хостинга и деплоя (пример) 

# Быстрый старт
## Клонирование репозитория

git clone https://github.com/yourusername/detect.git
cd detect
## Настройка окружения
Создайте файл .env по образцу .env.example

Заполните переменные окружения: настройки БД, Redis, ключи API, секреты

## Запуск локально через Docker Compose

docker-compose build
docker-compose up -d

## Миграции базы данных
docker-compose exec backend poetry run python manage.py migrate
# Тестирование

docker-compose exec backend poetry run pytest

# Структура проекта
core/ — основное приложение, загрузка, OCR, перевод, наложение текста

users/ — управление пользователями и аутентификация

config/ — конфигурации Django, Celery, URL маршруты

static/ и media/ — публичные и загруженные файлы

Dockerfile, docker-compose.yml — контейнеризация

.github/workflows/ci-cd.yml — автоматизация тестов, сборки, деплоя

tests/ — тесты проекта с использованием pytest

CI/CD

# Реализован через GitHub Actions:

Линтинг кода (flake8)

Запуск тестов (pytest)

Сборка Docker-образов

Деплой на сервер через SSH

# Полезные команды

Запуск миграций:

docker-compose exec backend poetry run python manage.py migrate

Запуск тестов:

docker-compose exec backend poetry run pytest -v

Посмотреть логи nginx:

docker-compose logs -f nginx

Перезапустить celery worker:

docker-compose restart celery

# Контакты и поддержка
Email: mymillions@ya.ru 

Репозиторий GitHub: https://github.com/carplatinum/detect

# Лицензия
MIT License