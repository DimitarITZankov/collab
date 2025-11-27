#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Wait for the database to be ready
echo "Entrypoint script: Waiting for PostgreSQL..."

# This loop checks if the database is ready by trying to connect to it.
until PGPASSWORD="$DB_PASSWORD" psql -h "db" -U "$DB_USER" -c '\q'; do
  >&2 echo "Entrypoint script: PostgreSQL is unavailable - sleeping 1s"
  sleep 1
done

echo "Entrypoint script: PostgreSQL started"

# Apply database migrations
python manage.py migrate --noinput

# Start the Gunicorn server
exec gunicorn --bind 0.0.0.0:8000 --workers 3 config.wsgi:application