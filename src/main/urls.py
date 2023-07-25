from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("test", views.test, name="test"),
    path("result", views.result, name="result"),
]
