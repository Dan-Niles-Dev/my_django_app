from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Routes the base URL of the app to the home view
]
