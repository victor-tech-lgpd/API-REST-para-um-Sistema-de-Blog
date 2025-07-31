API REST para um Sistema de Blog
Esta é uma API RESTful completa desenvolvida com Django e Django REST Framework. Ela fornece um back-end para um sistema de blog, permitindo operações de CRUD (Criar, Ler, Atualizar, Deletar) para posts e comentários, com autenticação de usuário baseada em JWT (JSON Web Tokens).

✨ Funcionalidades
Autenticação de usuário com JSON Web Tokens (JWT).

Endpoints completos para gerenciar Posts.

Endpoints para adicionar e visualizar Comentários em posts.

Sistema de permissões: Leitura pública, escrita apenas para usuários autenticados.

Estrutura de projeto organizada e segura, com segredos protegidos.

🛠️ Tecnologias Utilizadas
Backend: Python, Django

API: Django REST Framework

Autenticação: Simple JWT for DRF

Banco de Dados: SQLite3 (padrão de desenvolvimento)

🚀 Configuração do Ambiente
Siga os passos abaixo para configurar e rodar o projeto localmente.

1. Clonar o Repositório

Bash

git clone https://github.com/victor-tech-lgpd/API-REST-para-um-Sistema-de-Blog.git
cd API-REST-para-um-Sistema-de-Blog
2. Criar e Ativar o Ambiente Virtual

Windows (PowerShell):

PowerShell

python -m venv .venv
.\.venv\Scripts\Activate.ps1
Linux / macOS:

Bash

python3 -m venv .venv
source .venv/bin/activate
3. Instalar as Dependências

Use o arquivo requirements.txt para instalar todos os pacotes necessários.

Bash

pip install -r requirements.txt
4. Configurar as Variáveis de Ambiente

O projeto usa um arquivo .env para gerenciar segredos.

Copie o arquivo de exemplo:

Bash

# Windows
copy .env.example .env

# Linux / macOS
cp .env.example .env
Abra o arquivo .env e adicione uma SECRET_KEY. Você pode gerar uma facilmente neste site ou via linha de comando.

5. Aplicar as Migrações do Banco de Dados

Este comando cria as tabelas do banco de dados.

Bash

python manage.py migrate
6. Criar um Superusuário

Você precisará de um usuário para obter um token de autenticação.

Bash

python manage.py createsuperuser
Siga as instruções para criar seu usuário e senha.

7. Iniciar o Servidor

Bash

python manage.py runserver
A API estará disponível em http://127.0.0.1:8000/.

⚙️ Como Usar a API
1. Obter um Token de Autenticação
Envie uma requisição POST para o endpoint /api/token/ com seu usuário e senha.

Bash

curl -X POST -H "Content-Type: application/json" \
-d '{"username": "seu-usuario", "password": "sua-senha"}' \
http://127.0.0.1:8000/api/token/
A resposta conterá seus tokens access e refresh.

2. Exemplo: Criar um Novo Post
Para criar um post, envie uma requisição POST para /api/posts/, incluindo o token de acesso no cabeçalho Authorization.

Bash

# Substitua SEU_TOKEN_DE_ACESSO pelo token obtido no passo anterior
curl -X POST -H "Content-Type: application/json" \
-H "Authorization: Bearer SEU_TOKEN_DE_ACESSO" \
-d '{"title": "Título do Meu Post", "body": "Conteúdo interessante aqui."}' \
http://127.0.0.1:8000/api/posts/
Endpoints da API
Endpoint	Método HTTP	Descrição	Autenticação Necessária?
/api/token/	POST	Obtém um par de tokens JWT.	Não
/api/token/refresh/	POST	Atualiza um token de acesso expirado.	Não
/api/posts/	GET	Lista todos os posts.	Não
/api/posts/	POST	Cria um novo post.	Sim (Bearer Token)
/api/posts/<id>/	GET	Retorna um post específico.	Não
/api/posts/<id>/	PUT, PATCH	Atualiza um post específico.	Sim (Bearer Token)
/api/posts/<id>/	DELETE	Apaga um post específico.	Sim (Bearer Token)
/api/comments/	POST	Cria um novo comentário para um post.	Sim (Bearer Token)

Exportar para as Planilhas
🧪 Testes
Para rodar os testes automatizados e garantir a integridade da aplicação, use o comando:

Bash

python manage.py test
