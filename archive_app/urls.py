from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),

    path("account/sign-up/", views.account_sign_up_view, name="account sign up"),
    path("account/log-in/", views.account_login_view, name="account log in"),

    path("account/", views.account_view, name="account"),
    path("account/logout/", LogoutView.as_view(next_page="home"), name="log out"),
    path("account/change-email/", views.change_email_view, name="change email"),
    path("account/change-password/", views.change_password_view, name="change password"),
    path("account/delete/", views.delete_account, name="delete account"),

    path("artist/sign-up", views.artist_sign_up_view, name="artist sign up")
]