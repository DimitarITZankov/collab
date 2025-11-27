## Setup: Step-By-Step Actions Taken

#### Initialize Django project
Create virtual environment instance/folder
`python3 -m venv venv`

Create .gitignore file in root directory, ignore /venv

Activate python virtual environment
`source venv/bin/activate`

Install Django up to date version
`pip install django`

Create 'backend' directory
`mkdir backend`

Create Django project with core directory 'config' inside directory 'backend'
`django-admin startproject config backend`

Move into /backend directory
`cd backend`

Test development server, visit in browser to see if it works
`python manage.py runserver`

Create .gitignore file for /backend, add __pycache__/ to .gitignore

Create Django app for API
`python manage.py startapp api`

Add 'api' to INSTALLED_APPS inside settings.py

Let's outsource sensitive environment variables and adhere to [Twelve Factor principles](https://www.12factor.net/codebase):
Create `.env` and `.env.example` files in the `/backend` directory
`pip install python-dotenv`
Change `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS` and `DATABASES` values in `settings.py` to import `.env.local` file variable values.
Also, In settings.py, update DATABASES.ENGINE to use postgresql

#### Migrate from SQLite3 to Postgres DB
Install pyscopg (really psycopg3 ...but not psycopg2)
`pip install psycopg`








#### Containerize Django
Create Dockerfile in /backend directory

#### Useful commands/operations
Example: This will run `python manage.py makemigrations` inside the `backend` container
`docker-compose run backend <COMMAND (e.g. python manage.py makemigrations)>`

Test Dockerfile to see how it builds:
`docker build . -t my-django-image-test` (while inside /backend directory ~or whichever you're testing)