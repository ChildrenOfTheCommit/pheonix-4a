# 🚀 Alpha Centauri – Server

[![Django](https://img.shields.io/badge/Django-6.1-092e20?logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.18.0-a30000?logo=django)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169e1?logo=postgresql)](https://www.postgresql.org/)
[![JWT](https://img.shields.io/badge/JWT-2.13.0-000000?logo=jsonwebtokens)](https://jwt.io/)
[![Python](https://img.shields.io/badge/Python-3.12-3776ab?logo=python)](https://www.python.org/)

---

## 🚀 About

**Alpha Centauri** is a centralized platform for the Interstellar Exploration Agency (IEA) — a system where explorers can record newly discovered planets across the galaxy.

This repository contains the **backend API server** built with Django and Django REST Framework. It handles authentication, data management, and business logic for the entire platform.

---

## ✨ Core Features

- **Authentication** – Register, login, and JWT-based session management
- **Explorer Directory** – Manage and browse registered explorers
- **Planet Discoveries** – Full CRUD operations for planet records
- **Planet Classes** – Commanders can manage classifications
- **Dashboard** – Provides statistics and recent activity data

---

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Django** | 6.1 | Backend framework |
| **Django REST Framework** | 3.18.0 | API development |
| **djangorestframework-simplejwt** | 5.5.1 | JWT authentication |
| **PostgreSQL** | 16 | Production database |
| **PyJWT** | 2.13.0 | JWT encoding/decoding |
| **psycopg** | 3.3.4 | PostgreSQL adapter |

---

## 🏁 Quick Start

```bash
# Clone the repository
git clone https://github.com/ChildrenOfTheCommit/AlphaCentauri-Server.git
cd AlphaCentauri-Server

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

The API will be available at `http://localhost:8000`.

---

**GitHub:** [ChildrenOfTheCommit/AlphaCentauri-Server](https://github.com/ChildrenOfTheCommit/AlphaCentauri-Server)

