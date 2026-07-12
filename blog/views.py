# blog/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Article


def liste_articles(request):
    articles = Article.objects.filter(statut="publie").select_related("auteur", "categorie")
    return render(request, "blog/liste_articles.html", {"articles": articles})


def detail_article(request, slug):
    article = get_object_or_404(Article, slug=slug, statut="publie")
    return render(request, "blog/detail_article.html", {"article": article})


def api_articles(request):
    articles = Article.objects.filter(statut="publie").values("titre", "slug", "date_creation")
    return JsonResponse(list(articles), safe=False)