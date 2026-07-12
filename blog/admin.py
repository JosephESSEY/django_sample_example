from django.contrib import admin
from .models import Categorie, Article, Commentaire


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ["nom", "slug"]
    prepopulated_fields = {"slug": ("nom",)}   # génère le slug automatiquement depuis le nom, en JS côté admin


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["titre", "auteur", "categorie", "statut", "date_creation"]
    list_filter = ["statut", "categorie", "date_creation"]
    search_fields = ["titre", "contenu"]
    prepopulated_fields = {"slug": ("titre",)}
    date_hierarchy = "date_creation"


@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ["auteur", "article", "approuve", "date_creation"]
    list_filter = ["approuve"]
    actions = ["approuver_commentaires"]

    @admin.action(description="Approuver les commentaires sélectionnés")
    def approuver_commentaires(self, request, queryset):
        queryset.update(approuve=True)