from django.urls import path
from . import views

# url configuration module
# Mapping URLs
urlpatterns = [
    path('', views.say_hello)
]