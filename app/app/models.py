from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
	# Custom Manager for the users
	# Providing the other fields by using the extra_fields
	def create_user(self,email,password=None,**extra_fields):
		if not email:
			raise ValueError("Every user must have an email")
		# Normalize the email and pass all the fields to the variable user
		user = self.model(email=self.normalize_email(email),**extra_fields)
		# Hashes the password
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,email,password, **extra_fields):
		user = self.create_user(email,password, **extra_fields)
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

	# Better approach for create_superuser function :

''' def create_superuser(self, email, password, **extra_fields):
	    extra_fields.setdefault('is_staff', True)
	    extra_fields.setdefault('is_superuser', True)
	    	if extra_fields.get('is_staff') is not True:
	        	raise ValueError('Superuser must have is_staff=True.')
	    	if extra_fields.get('is_superuser') is not True:
	        	raise ValueError('Superuser must have is_superuser=True.')
	    return self.create_user(email, password, **extra_fields)
'''

class CustomUser(AbstractBaseUser,PermissionsMixin):
	# Create custom user model
	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=50, unique=True)
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
		return self.email