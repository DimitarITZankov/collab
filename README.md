# collab

For Development:
`docker compose up --build`
Django serves backend, Vite

For Production:
`docker compose -f docker-compose.prod.yml up --build -d`
Gunicorn + Django backend, Vite + Nginx frontend