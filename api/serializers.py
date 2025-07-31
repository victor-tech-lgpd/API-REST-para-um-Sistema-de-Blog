# api/serializers.py
from rest_framework import serializers
# CORREÇÃO: Importa os modelos da aplicação 'blog'
from blog.models import Post, Comment
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # O campo 'active' do modelo original do blog foi omitido aqui,
        # mas pode ser adicionado se a API precisar expô-lo.
        fields = ['id', 'author_name', 'body', 'created_on', 'post']
        read_only_fields = ['author_name']


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author', 'created_on', 'last_modified', 'comments']