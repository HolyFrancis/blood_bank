from django.urls import path

from apps.views import user, home

urlpatterns = [
    path("", home.home, name="home"),
    path("register", user.register, name="register"),
]
