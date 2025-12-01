# Add requirements.txt file with all the dependencies needed for now

# Initialize Dockerfile and compose.yaml file

# Create project and app using docker compose

# Remove the SQLite database due to switching to PostgreSQL

# Edit the settings.py 
	- Add the app's name, rest_framework and rest_framework_simplejwt to INSTALLED_APPS
	- Edit the DATABASE

# Add "wait_for_db.py" script -> /app/app/management/commands/wait_for_db.py
	- Add into the compose.yaml file to execute the script and then migrate before runserver

# Implement the JWT authentication and create register endpoint
	- Initialize at the bottom of the file the default authentication class of rest framework by: 
	REST_FRAMEWORK = {'DEFAULT_AUTHENTICATION_CLASSES':('rest_framework_simplejwt.authentication.JWTAuthentication',),}