from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("start-test", views.start_test, name="start_test"),
    path("test", views.test, name="test"),
    path("next", views.next, name="next"),
    path("result", views.result, name="result"),
]
