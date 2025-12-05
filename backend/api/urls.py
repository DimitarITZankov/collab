from django.urls import path
from .views import CreateUserView, login_view, logout_view

urlpatterns = [
    path('user/register/', CreateUserView.as_view(), name="register"),
    path("login/", login_view),
    path("logout/", logout_view),
]