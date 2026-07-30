## Pokémon API

## 📌 | 🇺🇸 Description | 🇧🇷 Descrição  
 - 🇺🇸 | REST API developed with Python to manage data from the first generation of Pokémon, consuming info from a public API.
 - 🇧🇷 | API REST desenvolvida com Python para gerenciamento de dados da primeira geração de Pokémon, consumindo informações de uma API pública.

## 🎯 | 🇺🇸 Project purpose | 🇧🇷 Propósito do projeto 
  - 🇺🇸 | A learning project focused on building a REST API using Python, exploring backend development, database integration and asynchronous tasks.
  - 🇧🇷 | Um projeto de aprendizagem focado na criação de uma API REST utilizando Python, explorando desenvolvimento backend, integração com banco de dados e tarefas assíncronas.

## ⚙️ | 🇺🇸 Technologies | 🇧🇷 Tecnologias
  - Python
  - FastAPI
  - SQLAlchemy
  - PostgreSQL
  - Redis
  - Celery
  - Pytest
  - Docker / Podman

## 📸 | 🇺🇸 Images | 🇧🇷 Imagens  
  > <img width="800" height="513" alt="Testing" src="https://github.com/user-attachments/assets/7a78c847-38f2-4029-ab3a-de5feb9bcd89" />

  > <img width="800" height="513" alt="Page 2" src="https://github.com/user-attachments/assets/e1547aa4-b1d2-4887-b4d8-9c3a524a66be" />

  > <img width="800" height="513" alt="Page Pokemon" src="https://github.com/user-attachments/assets/bb1589e4-531a-498a-8fe9-449aa694c3c6" />

## 🚀 | 🇺🇸 Access via Railway | 🇧🇷 Acesso via Railway
> API - https://pokemon-python-production.up.railway.app/pokemon

> Swagger Doc - https://pokemon-python-production.up.railway.app/docs

## 🚀 | 🇺🇸 How to run the project locally | 🇧🇷 Instruções para rodar localmente
  > - 🇺🇸 | 1. Download the .zip file from the GitHub repository (https://github.com/Clique-N/Pokemon-Python).
  > - 🇧🇷 | 1. Faça o download do arquivo .zip no repositório do GitHub (https://github.com/Clique-N/Pokemon-Python).
  
  > - 🇺🇸 | 2. Extract the .zip file to a folder on your computer, then open the project in VS Code.
  > - 🇧🇷 | 2. Extraia o arquivo .zip na pasta do seu computador, e em seguida abra no VS Code.

  > - 🇺🇸 | 3. Create the environment file: `.env`.
  > - 🇧🇷 | 3. Criar o arquivo de ambiente: `.env`
  > - `.env` example:
  ```env
    DATABASE_URL=postgresql+psycopg://postgres:postgres@postgres:5432/pokemon
    REDIS_HOST=redis
    REDIS_PORT=6379
    REDIS_URL=redis://redis:6379/0
  ```
  > - 🇺🇸 | 4. Open the terminal and run the following command to run the containers: `podman compose up --build` / `docker compose up --build`.
  > - 🇧🇷 | 4. Abra o terminal e rode os containers:  `podman compose up --build` / `docker compose up --build`.
  
  > - 🇺🇸 | 5. The API will be available at: `http://localhost:8000`.
  > - 🇧🇷 | 5. A API estará disponível em: `http://localhost:8000`.

  > - 🇺🇸 | 🇧🇷 | 5.1. API Endpoints.
  > - |GET| `/`                 | 🇺🇸 - Starts Pokemon database population task. | 🇧🇷 - Preenche o banco de dados com Pokemon.
  > - |GET| `/status/{task_id}` | 🇺🇸 - Checks Celery task status.               | 🇧🇷 - Verifica o status do Celery a tarefa.
  > - |GET| `/pokemon`          | 🇺🇸 - Lists Pokemon with pagination.           | 🇧🇷 - Lista de Pokemon com paginação.
  > - |GET| `/pokemon/{id}`     | 🇺🇸 - Returns a specific Pokemon by ID.        | 🇧🇷 - Retorna um Pokemon especifico pelo seu ID.
  
  > - 🇺🇸 | 6. To run tests, open the terminal and run the following command: `pytest --cov`.
  > - 🇧🇷 | 6. Para os testes, abra o terminal e digite o comando: `pytest --cov`.


## 📝 | 🇺🇸 What I learned | 🇧🇷 Meus aprendizados
  - 🇺🇸 | Building a REST API, consuming data from a public API, creating and managing a database, and integrating asynchronous tasks using Celery and Redis.
  - 🇧🇷 | Criar uma API REST, consumir dados de uma API pública, criar e gerenciar um banco de dados e integrar tarefas assíncronas utilizando Celery e Redis. 
