#!/bin/sh

set -e

echo "Running migrations..."
/usr/src/connect/.venv/bin/python manage.py migrate --no-input

echo "Creating superuser (if not exists)..."
/usr/src/connect/.venv/bin/python manage.py createsuperuser --no-input || true

echo "Starting the app..."
APP_PORT=${APP_PORT:-8000}
/usr/src/connect/.venv/bin/daphne backend.asgi:application --bind 0.0.0.0 --port $APP_PORT