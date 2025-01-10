# Desafio_Backend_Eject

## 1. Sobre o Projeto: Objetivo e funcionalidades principais.
<p style="text-align: justify;">
Este projeto tem como objetivo criar uma API REST para um Mini-Twitter, contendo as funcionalidades básicas de realizar criação de usuários, fazer login, criar postagens, além de fazer comentários e curtidas nas postagens.
</p>

## 2. Instalação e Execução: Passo a passo para configurar e rodar a aplicação.

<p style="text-align: justify;">
Primeiramente é necessário entrar no diretório do projeto, após isso é necessário executar os seguintes comandos em sequência.
</p>

Comando para entrar no ambiente virtual caso esteja no Windows: 
```
	venv\Scripts\activate.bat
```
Comando para entrar no ambiente virtual caso esteja no Linux ou MacOS:
```	    
    source venv/bin/activate
```
Comando para instalar as depêndencias:
```	
    pip install -r requirements.txt
```
Comandos para checar alterações e criar o banco de dados:
```
	python manage.py makegrations
	
	python manage.py migrate
```
Comando para rodar a aplicação:
```
	python manage.py runserver
```

## 3. Dependências: Principais bibliotecas e versões.
- [Django](https://www.djangoproject.com/) - Framework web em Python.
- [Django REST Framework](https://www.django-rest-framework.org/) - Ferramenta para construção de APIs RESTful.
- [Django REST Framework Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - Plugin para gerar JSON Web Tokens para Authentication
- [Django REST Framework drf-yasg](https://github.com/axnsan12/drf-yasg/) - Ferramenta para gerar documentação Swagger

## 4. Documentação da API: Instruções para acessar o Swagger com detalhes dos endpoints.
<p style="text-align: justify;">
Primeiramente é necessário executar todos os comandos para instalar as dependências e rodar a aplicação, após isso é necessário apenas acessar o endpoint: 
</p>

```
http://<endereço IP local>:<Porta do servidor web>/swagger/
```

## Colaboradores da API
1. [Cipriano José Da Silva Neto](https://github.com/MCipris)

## Mentores
1. [Paulo Vinícius](https://github.com/Paulo-Vinicius-m)