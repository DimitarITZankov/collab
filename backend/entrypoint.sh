#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

DB_HOST=$DATABASE_HOST
DB_PORT=$DATABASE_PORT

echo "Entrypoint script: Waiting for PostgreSQL at $DB_HOST:$DB_PORT..."

# This loop checks if the database is ready by trying to connect to it.
until printf "" 2>>/dev/null >>/dev/tcp/$DB_HOST/$DB_PORT; do
  echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done

echo "Entrypoint script: PostgreSQL started - executing command"

python manage.py migrate --noinput

exec "$@"