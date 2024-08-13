from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blogpost/<slug:slug>/", views.view_post, name="blogpost"),
]
