# blog/urls.py
from rest_framework.routers import DefaultRouter
from .views import CategorieViewSet, ArticleViewSet, CommentaireViewSet

router = DefaultRouter()
router.register("categories", CategorieViewSet)
router.register("articles", ArticleViewSet)
router.register("commentaires", CommentaireViewSet)

urlpatterns = router.urls