from django.urls import path

from . import views

app_name = "ecomap"
urlpatterns = [
    path("homepage/", views.homepage, name="homepage"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    path("login/", views.login, name="hangman"),
    path("hangman/", views.hangman, name="hangman"),
    path("qrcode/", views.qrcode, name="qrcode"),
]
