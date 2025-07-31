# meuprojeto/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet, CommentViewSet  # Ajuste conforme o local dos seus ViewSets

# Criar o roteador para os ViewSets
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

# Definir as URLs
urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para o painel de administração
    path('api/', include(router.urls)),  # Inclui as rotas geradas pelo roteador
]