from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ["nom"]

    def __str__(self):
        return self.nom


class Article(models.Model):
    class Statut(models.TextChoices):
        BROUILLON = "brouillon", "Brouillon"
        PUBLIE = "publie", "Publié"

    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    contenu = models.TextField()
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, related_name="articles")
    statut = models.CharField(max_length=10, choices=Statut.choices, default=Statut.BROUILLON)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_maj = models.DateTimeField(auto_now=True)
    date_publication = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-date_creation"]

    def __str__(self):
        return self.titre

    def publier(self):
        self.statut = self.Statut.PUBLIE
        self.date_publication = timezone.now()
        self.save()


class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="commentaires")
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    approuve = models.BooleanField(default=False)

    class Meta:
        ordering = ["date_creation"]

    def __str__(self):
        return f"Commentaire de {self.auteur} sur {self.article}"