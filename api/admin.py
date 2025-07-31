# api/admin.py
from django.contrib import admin
# CORREÇÃO: Importa os modelos centralizados do 'blog'
from blog.models import Post, Comment

# Registra os modelos para que apareçam no site de administração do Django
admin.site.register(Post)
admin.site.register(Comment)