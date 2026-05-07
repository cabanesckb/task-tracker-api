from django.urls import path
from . import api_views

app_name = 'auth'
urlpatterns = [
    path("register/", api_views.Register.as_view(), name="register"),
]