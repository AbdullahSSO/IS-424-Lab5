from django.urls import path
from . import views
from django import forms

app_name = "myApp"
urlpatterns = [
    path("", views.index, name="index"),
    path("add" , views.add, name="add")
]