from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
	# Custom Manager for the users
	# Providing the other fields by using the extra_fields
	def create_user(self,email,password=None,role="user",**extra_fields):
		if not email:
			raise ValueError("Every user must have an email")
		extra_fields.setdefault('role', role) # Set by default the role USER
		# Normalize the email and pass all the fields to the variable user
		user = self.model(email=self.normalize_email(email),**extra_fields)
		# Hashes the password
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('role', CustomUser.Roles.ADMIN) # Set the ADMIN role by default
		extra_fields.setdefault('is_staff', True) # Set is_staff = True
		extra_fields.setdefault('is_superuser', True) #Set is_superuser = True
		return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser,PermissionsMixin):
	# Create roles with permissions using TextChoices provided by Django (django.db.models) used to define enumerations for model fields
	class Roles(models.TextChoices):
		# Initialize the different roles
		ADMIN = "admin", "Admin"
		MODERATOR = "moderator", "Moderator"
		USER = "user", "User"

	# Create custom user model
	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=50, unique=True)
	role = models.CharField(max_length=20,choices=Roles.choices, default=Roles.USER)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = UserManager()

	# Assign the login field and the required fields to the custom user manager
	# Users will be logging in using their email
	# Require every user to put name and username
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name','username']

	# Helper functions
	def get_full_name(self):
		return self.name

	def get_short_name(self):
		return self.name

	def __str__(self):
		return f"{self.email} ({self.role})"