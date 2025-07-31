# api/tests.py
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from blog.models import Post

class PostAPITestCase(APITestCase):
    
    def setUp(self):
        """Cria um usuário de teste que será usado em vários testes."""
        self.user = User.objects.create_user(username='testuser', password='testpassword123')

    def test_list_posts_unauthenticated(self):
        """Garante que qualquer pessoa (mesmo não autenticada) pode listar os posts."""
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post_unauthenticated(self):
        """Garante que um usuário não autenticado NÃO pode criar um post."""
        data = {'title': 'Post de Teste', 'body': 'Conteúdo do teste'}
        response = self.client.post('/api/posts/', data, format='json')
        # Deverá retornar 401 Unauthorized, pois não fornecemos token
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_post_authenticated(self):
        """Garante que um usuário autenticado PODE criar um post."""
        # Força a autenticação do cliente com o usuário de teste
        self.client.force_authenticate(user=self.user)
        
        data = {'title': 'Post Autenticado', 'body': 'Conteúdo criado por usuário logado.'}
        response = self.client.post('/api/posts/', data, format='json')
        
        # Verifica se o post foi criado com sucesso
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Verifica se o autor do post é o usuário que fez a requisição
        self.assertEqual(response.data['author']['username'], self.user.username)
        # Verifica se o post realmente existe no banco de dados
        self.assertTrue(Post.objects.filter(title='Post Autenticado').exists())