from rest_framework import serializers
from .models import Categorie, Article, Commentaire

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ["id", "nom", "slug"]

class ArticleSerializer(serializers.ModelSerializer):
    auteur_details = serializers.ReadOnlyField(source="auteur.username")
    categorie_details = serializers.ReadOnlyField(source="categorie.nom")
    
    class Meta:
        model = Article
        fields = [
            "id", "titre", "slug", "contenu", "auteur", "auteur_details",
            "categorie", "categorie_details", "statut", "date_creation",
            "date_maj", "date_publication"
        ]
        read_only_fields = ["auteur", "date_creation", "date_maj", "date_publication"]

class CommentaireSerializer(serializers.ModelSerializer):
    auteur_details = serializers.ReadOnlyField(source="auteur.username")
    
    class Meta:
        model = Commentaire
        fields = ["id", "article", "auteur", "auteur_details", "contenu", "date_creation", "approuve"]
        read_only_fields = ["auteur", "date_creation"]
