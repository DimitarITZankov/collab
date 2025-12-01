from rest_framework import serializers
from app import models
from django.contrib.auth import get_user_model

# Return my custom user model 
User = get_user_model()

# Create serializer for registering users
class RegisterSerializer(serializers.ModelSerializer):
	# Set password to be write_only and not return it as response
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['email', 'name', 'username','password']

	# Override the create function
	def create(self,validated_data):
		user = User.objects.create_user(email=validated_data['email'],name=validated_data['name'],password=validated_data['password'])
		return user

# Other way to override the create function
''' 
def create(self, validated_data):
	return User.objects.create_user(**validated_data)
'''
