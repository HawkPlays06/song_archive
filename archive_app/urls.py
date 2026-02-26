from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("log-in/", views.log_in_view, name="log in")
]