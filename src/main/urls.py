from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("assessment", views.assessment, name="assessment"),
    path("next", views.next, name="next"),
    path("result", views.result, name="result"),
    path("finish-assessment", views.finish_assessment, name="finish_assessment"),
]
