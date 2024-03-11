# TODO LIST (Em desenvolvimento)
Este é um projeto feito em Python utilizando Flask, possui um banco de dados para armazenar informações de tarefas.

- [Requisitos](#requisitos)
- [Configuração do Ambiente Virtual](#configuração-do-ambiente-virtual)
- [Configuração do Banco de Dados](#configuração-do-banco-de-dados)
- [Executando o Projeto](#executando-o-projeto)
- [Rotas](#rotas)

# Configuração do Ambiente Virtual
Clone o repositório:
```
git clone https://github.com/ilvmikan/todo_list.git
cd todo_list
```
Crie e ative um ambiente virtual:
```
# No Windows
python -m venv venv 
venv\Scripts\activate

# No Linux/Mac
source venv/bin/activate
```

Instale as dependências do projeto:
```
pip install -r requirements.txt
```

# Configuração do Banco de Dados
Este projeto utiliza um banco de dados SQLite como exemplo. Se necessário, ajuste as configurações do banco de dados no arquivo `__init__.py` de acordo com suas preferências.

Execute as migrações para criar as tabelas no banco de dados:

```
flask db init
flask db migrate
flask db upgrade
```

# Executando o Projeto
Agora que o ambiente virtual está configurado e o banco de dados inicializado, você pode iniciar o servidor Flask:
```
flask run
```
O servidor estará disponível em `http://127.0.0.1:5000/` 
Acesse este URL em seu navegador para interagir com o aplicativo.


# Rotas
O aplicativo possui quatro rotas principais, cada uma correspondendo a uma funcionalidade específica do seu projeto Flask. Aqui estão as descrições breves de cada rota:

## /index ou /
- Esta rota exibe uma visão resumida de todas as tarefas no sistema. Inclui informações como o título da tarefa, data de criação, estado atual etc.

## /create

- Esta rota é responsável por permitir a criação de novas tarefas no aplicativo. Ela exibe um formulário/interface que permite aos usuários inserirem as informações necessárias para adicionar uma nova tarefa ao sistema.

## /delete

- Essa rota lida com a exclusão de tarefas do aplicativo.
## /edit

- Aqui, os usuários podem acessar uma tarefa específica para fazer alterações ou atualizações.