# Gerenciador de Tarefas

Um projeto simples de gerenciamento de tarefas desenvolvido com Django para o backend e um frontend minimalista integrado com HTML, CSS e JavaScript. Ele oferece funcionalidades básicas de CRUD (Criar, Ler, Atualizar, Deletar) de tarefas e associa essas tarefas a pessoas.

---

## **Índice**

1. [Funcionalidades](#funcionalidades)
2. [Estrutura do Projeto](#estrutura-do-projeto)
3. [Configuração do Ambiente](#configuração-do-ambiente)
4. [Como Executar](#como-executar)
5. [Endpoints da API](#endpoints-da-api)
6. [Tecnologias Utilizadas](#tecnologias-utilizadas)

---

## **Funcionalidades**

- **Tarefas**:
  - Criar uma nova tarefa com título, descrição, prazo e situação.
  - Listar todas as tarefas cadastradas.
  - Atualizar informações de uma tarefa existente.
  - Deletar tarefas.
  
- **Pessoas**:
  - Gerenciar pessoas responsáveis pelas tarefas.

---

## **Estrutura do Projeto**

```plaintext
gerenciador-tarefas/
├── manage.py
├── setup/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tarefas/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializer.py
│   ├── tests.py
│   └── views.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── app.js
├── staticfiles/
│   └── (arquivos estáticos coletados)
├── db.sqlite3
├── requirements.txt
└── README.md
```

# Configuração do Ambiente

### Pré-requisitos:
- **Python 3.10+**
- **Pip** (gerenciador de pacotes do Python)
- **Virtualenv** (opcional, mas recomendado)

---


# Endpoints da API

## Tarefas

### Listar todas as tarefas
**GET** `/api/tarefas/`

---

### Criar uma nova tarefa
**POST** `/api/tarefas/`

**Body**:
```json
{
    "titulo": "Nova tarefa",
    "descricao": "Descrição da tarefa",
    "prazo_para_conclusao": "2025-01-30T12:00:00Z",
    "situacao": "P",
    "pessoa": null
}
```

---

### Atualizar uma tarefa existente
**PUT** `/api/tarefas/{id}/`

**Body**:
```json
{
    "titulo": "Tarefa atualizada",
    "descricao": "Descrição atualizada",
    "prazo_para_conclusao": "2025-01-30T12:00:00Z",
    "situacao": "C",
    "pessoa": null
}
```

---

### Excluir uma tarefa
**DELETE** `/api/tarefas/{id}/`

---

## Pessoas

### Listar todas as pessoas
**GET** `/api/pessoas/`

---

### Criar uma nova pessoa
**POST** `/api/pessoas/`

**Body**:
```json
{
    "nome": "Maria",
    "sobrenome": "Souza",
    "email": "maria@email.com"
}
```

---

### Atualizar uma pessoa existente
**PUT** `/api/pessoas/{id}/`

**Body**:
```json
{
    "nome": "Maria",
    "sobrenome": "Silva",
    "email": "maria@email.com"
}
```

---

### Excluir uma pessoa
**DELETE** `/api/pessoas/{id}/`

