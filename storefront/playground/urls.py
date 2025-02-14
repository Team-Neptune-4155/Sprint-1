from django.urls import path
from . import views

# url configuration module
# Mapping URLs
urlpatterns = [
    path('hello/', views.say_hello)
]