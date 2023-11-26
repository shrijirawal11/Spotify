from django.urls import path, include
from user.views import home

urlpatterns = [
    path('', home, name="home"),
]

