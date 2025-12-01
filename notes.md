# Add requirements.txt file with all the dependencies needed for now

# Initialize Dockerfile and compose.yaml file

# Create project and app using docker compose

# Remove the SQLite database due to switching to PostgreSQL

# Edit the settings.py 
	- Add the app's name, rest_framework to INSTALLED_APPS
	- Edit the DATABASE

# Add "wait_for_db.py" script -> /app/app/management/commands/wait_for_db.py
	- Add into the compose.yaml file to execute the script and then migrate before runserver

# Implement the JWT authentication and create register endpoint
	- Initialize at the bottom of the file the default authentication class of rest framework by: 
	REST_FRAMEWORK = {'DEFAULT_AUTHENTICATION_CLASSES':('rest_framework_simplejwt.authentication.JWTAuthentication',),}
	- Add to the INSTALLED_APPS => rest_framework_simplejwt
	- Add /api endpoint to the project's urls.py file
	- Add /token and /refresh endpoints for the JWT authentication into the app's urls.py file

# Create custom user model to test the JWT
	- Intialize in the settings.py the new auth model by: 
	AUTH_USER_MODEL = 'yourapp.CustomUser'
	- After creating the custom user model run makemigrations and then migrate to save everything

# Create Register API
	- Create serializer for registering users in the serializers.py file
	- Create RegisterAPIView in the views.py app's file