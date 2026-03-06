from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("sign-up/", views.sign_up_view, name="sign up"),
    path("log-in/", views.login_view, name="log in"),
    path("account/", views.account_view, name="account"),
    path("account/change-email", views.change_email_view, name="change email"),
    path("account/change-password", views.change_password_view, name="change password"),
]