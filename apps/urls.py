from django.urls import path

from apps.views import user

urlpatterns = [
    path("", user.loginview, name="login"),
    path("register", user.register, name="register"),
]
