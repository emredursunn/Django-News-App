from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("category/<slug:slug>/", views.get_news_by_category, name="category"),
    path("newsDetail/<slug:slug>", views.news_detail, name="newsDetail"),
]