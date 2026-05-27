# xuitter

Clone do Twitter/X construído como projeto de portfólio.

**Stack:** Python 3.10 · Django 5.0.7 · PostgreSQL 13 · Bootstrap 5.3.3 · pytest · factory-boy

---

## Funcionalidades

- Feed personalizado com posts de quem você segue
- Publicação de posts (até 140 caracteres)
- Curtidas em posts
- Sistema de follow/unfollow entre usuários
- Perfis com foto, bio e website
- Busca de posts e busca de usuários
- Cadastro, login e edição de perfil

---

## Arquitetura

```
Browser
   │
   ▼
Django :8000
   ├── /                → Feed (posts de quem você segue)
   ├── /profiles/       → Lista de todos os perfis
   ├── /profile/<id>    → Perfil + posts + follow/unfollow
   ├── /post/<id>       → Post individual
   ├── /search/         → Busca de posts
   └── /search_user/    → Busca de usuários
         │
         └── PostgreSQL :5432 (container Docker)
```

---

## Execução com Docker (recomendado)

```bash
docker compose up --build
```

Na primeira execução, em outro terminal:

```bash
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser  # opcional
```

---

## URLs de acesso

| Serviço   | URL                          |
| --------- | ---------------------------- |
| Aplicação | http://localhost:8000        |
| Admin     | http://localhost:8000/admin/ |

---

## Testes

```bash
pytest
```
