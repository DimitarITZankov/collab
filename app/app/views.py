from django.shortcuts import render
from rest_framework import generics, permissions, status
from app import serializers,models
from rest_framework.response import Response

# Register API
class RegisterAPIView(generics.CreateAPIView):
	serializer_class = serializers.RegisterSerializer
	permission_classes = [permissions.AllowAny]

	def create(self,request,*args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response({"message":"Successfully registered"}, status=status.HTTP_201_CREATED)
