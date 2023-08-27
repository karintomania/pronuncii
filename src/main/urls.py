from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("test", views.test, name="test"),
    path("next", views.next, name="next"),
    path("result", views.result, name="result"),
    path("finish-test", views.finish_test, name="finish_test"),
]
