from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from app import views

urlpatterns = [
	# JWT Endpoints
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

	# Register Endpoint
	path('register/', views.RegisterAPIView.as_view(),name='register')
]