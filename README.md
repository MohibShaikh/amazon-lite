# 📦 Amazon Lite

A minimal full-stack application for managing products and orders using **Django REST Framework** and **Vue 3 (Vite)**.

## Backend Setup (Django)

**1. Prerequisites**

* Python 3.10+
* [uv](https://github.com/astral-sh/uv) (Fast Python Package Manager)

**2. Installation**

```bash
# Clone the repo and enter backend directory
cd backend

# Install dependencies using uv
uv add django djangorestframework django-cors-headers
uv sync

```

**3. Configuration (`settings.py`)**
Ensure `corsheaders` is configured to allow the Vue dev server:

```python
INSTALLED_APPS = [..., "corsheaders", "rest_framework"]
MIDDLEWARE = ["corsheaders.middleware.CorsMiddleware", ...]
CORS_ALLOWED_ORIGINS = ["http://localhost:5173"]

```

**4. Run Server**

```bash
python manage.py migrate
python manage.py runserver

```

---

## 💻 Frontend Setup (Vue 3 + TS)

**1. Prerequisites**

* Node.js 18+
* npm or pnpm

**2. Installation**

```bash
cd frontend
npm install

```

**3. Environment Config**
Ensure `src/services/api.ts` points to your Django server:

* **Base URL:** `http://localhost:8000/api`

**4. Run Dev Server**

```bash
npm run dev

```

---

## 🛠 Features Implemented

### Backend (DRF)

* **Models:** Custom User, Product, Order, and OrderItem (with Many-to-Many through table).
* **Serializers:** Nested relationships and `SerializerMethodField` for calculated totals.
* **API Views:** Function-based views (`@api_view`) for CRUD operations on Products and Orders.

### Frontend (Vue 3)

* **Composition API:** Uses `<script setup lang="ts">` for modern reactivity.
* **Axios Service:** Centralized API client with TypeScript `interface` support.
* **Type Safety:** Strict type checking for API responses using `import type`.

---

## 📖 API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/products/` | List all products |
| `POST` | `/api/products/` | Create a new product |
| `GET` | `/api/orders/` | List all orders with items and totals |
| `DELETE` | `/api/orders/<id>/` | Delete an order |

---

Would you like me to add a section on how to create the **Superuser** or how to run the **Database Migrations** for a fresh start?
