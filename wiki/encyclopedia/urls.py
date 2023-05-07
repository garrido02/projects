from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.page, name="page"),
    path("search/q=<str:s>", views.search, name="search"),
    path("new", views.new, name="new"),
    path('edit/<str:name>', views.edit, name="edit"),
    path('random', views.random_page, name="random")
]