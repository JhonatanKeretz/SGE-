Projeto de desenvolvimento

Aplicação em Python com Django, com aplicação de API 

Desenvolvimento de um sistema de gestão de estoque com entrada e saída de produtos, com gráficos de informação de vendas e dos produtos.
Projeto para teste Everymind

Comandos para rodar projeto:

Adicionar VENV
python3 -m venv venv

Ativar VENV
source venv/bin/activate

Adicionar Django
pip install django

Criar as tabelas para banco

python manage.py makemigrations
python manage.py migrate

para dar start no projeto

python manage.py runserver

Precisar criar um usuário para acessar o sistema, pois nele contém sistema de login
python manage.py createsuperuser

Para instalação do projeto após baixar
aplicar pip freeze no terminal para executar os requerimentos.
