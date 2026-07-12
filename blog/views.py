from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Categorie, Article, Commentaire
from .serializers import CategorieSerializer, ArticleSerializer, CommentaireSerializer


class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

    @action(detail=True, methods=["get"])         # detail=True -> agit sur UN objet précis (/categories/1/articles/)
    def articles(self, request, pk=None):
        categorie = self.get_object()               # méthode héritée, récupère l'objet via l'id dans l'URL
        articles = categorie.articles.filter(statut="publie")
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])          # detail=False -> agit sur la COLLECTION (/categories/populaires/)
    def populaires(self, request):
        from django.db.models import Count
        categories = Categorie.objects.annotate(nb=Count("articles")).order_by("-nb")[:5]
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(auteur=self.request.user)


class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer

    def perform_create(self, serializer):
        serializer.save(auteur=self.request.user)