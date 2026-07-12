from django.urls import path
from . import views

urlpatterns = [
    path("", views.liste_articles, name="liste_articles"),
    path("articles/<slug:slug>/", views.detail_article, name="detail_article"),
    path("api/articles/", views.api_articles, name="api_articles"),
]