# 🚀 Alpha Centauri

### Interstellar Exploration Management System

## Story

**Year 2247**

Humanity has begun exploring distant star systems beyond Earth. The **Interstellar Exploration Agency (IEA)** has developed **Alpha Centauri**, a centralized platform used by explorers to record newly discovered planets across the galaxy.

Registered Explorers can submit discoveries, while Commanders oversee the database and ensure the accuracy of all recorded information.

---

# Roles

## Commander

* Manage Explorers
* Manage Planet Classifications
* View all discoveries
* Edit/Delete any discovery
* Dashboard statistics

## Explorer

* Register
* Login
* Manage Profile
* Submit Planet Discoveries
* Edit/Delete their own discoveries
* Browse the Explorer Directory

---

# Core Modules

## 1. Authentication

* Register
* Login
* JWT Authentication

---

## 2. Explorer Directory

View all registered explorers.

Fields

* Codename
* Name
* Avatar
* Join Date

---

## 3. Planet Discoveries ⭐

This is the heart of the project.

Each discovery contains:

* Planet Name
* Planet Class
* Galaxy
* Star System
* Description
* Discovery Date
* Cover Image
* Discovered By

---

## 4. Planet Classes

Commander manages classifications.

Examples

* Terrestrial
* Gas Giant
* Ice Planet
* Ocean World
* Desert Planet
* Lava Planet
* Artificial World

---

## 5. Dashboard

Show

* Explorers
* Planet Discoveries
* Planet Classes
* Recent Discoveries

---

# Database

Only four main tables.

```text
roles

users

planet_classes

planet_discoveries
```

Simple.

Easy to understand.

Easy to normalize.

---

# Technologies

Frontend

* Vue 3
* TypeScript
* Tailwind CSS
* Pinia
* Vue Router
* Axios

Backend

* Django
* Django REST Framework
* JWT

Database

* PostgreSQL
