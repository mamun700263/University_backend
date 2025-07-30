
# 🏛️ University Backend API

A scalable backend system for managing university operations — built with Django, DRF, and PostgreSQL. Supports full CRUD, role-based access (Admin, Teacher, Student), and future-proof extension plans. Modular, tested, and built for real-world deployment.

> **Built by**: [Mamun](https://github.com/mamun700263) (Backend Engineer)  
> **Status**: 🧠 Actively Developed

---

## 🚀 Project Highlights

| Feature             | Admin | Teacher | Student |
|---------------------|:-----:|:-------:|:-------:|
| 🔐 Role-Based Access |  ✅   |   ✅    |   ✅    |
| 👤 User Management   |  ✅   |   ❌    |   ❌    |
| 📚 Course Creation   |  ✅   |   ✅    |   ❌    |
| 📝 Grade Input       |  ✅   |   ✅    |   ❌    |
| 📈 Result Viewing    |  ✅   |   ✅    |   ✅    |
| 📅 Semester Control  |  ✅   |   ❌    |   ❌    |

---

## ⚙️ Tech Stack

- **Backend**: Django, Django REST Framework  
- **Database**: PostgreSQL  
- **Auth**: DRF Token Auth (custom)  
- **Testing**: `unittest` + `pytest`  
- **DevOps (Planned)**: Docker, GitHub Actions, Render/Railway  

---

## 🧠 Architecture Overview

```

university\_backend/
├── accounts/       # Auth system w/ custom user model
├── university/     # Core app: models, views, serializers
├── common/         # Utilities and shared logic
├── tests/          # API, unit, and integration tests
├── media/          # File uploads (if needed)
├── manage.py
├── requirements.txt
└── README.md

````

---

## 🧪 Setup Instructions

### 🔧 1. Install Dependencies

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
````

### 🛠️ 2. Apply Migrations

```bash
python manage.py migrate
```

### 🚦 3. Run Dev Server

```bash
python manage.py runserver
```

---

## 🔐 Auth Flow

* Token-based authentication (custom)
* Hit `/api/token/` with valid credentials to receive a token
* Use token in header:
  `Authorization: Token <your_token_here>`

---

## 🔭 Key API Endpoints

| Endpoint            | Method | Description         | Roles Allowed  |
| ------------------- | ------ | ------------------- | -------------- |
| `/api/users/`       | GET    | List users          | Admin only     |
| `/api/courses/`     | POST   | Create a course     | Admin, Teacher |
| `/api/grades/`      | POST   | Input grade         | Teacher        |
| `/api/grades/<id>/` | GET    | View student grades | Student        |

🔗 *Postman Collection: Coming Soon*
📁 *OpenAPI/Swagger docs: Planned under `/docs/`*

---

## 🧪 Testing Strategy

```bash
# Django default test runner
python manage.py test

# Or using pytest
pytest
```

Test Coverage:

* ✅ CRUD tests for universities
* ✅ Role-based access control
* ✅ Invalid input edge cases

---

## 📦 Deployment Roadmap

* [ ] Docker containerization
* [ ] Gunicorn + Nginx stack
* [ ] CI/CD via GitHub Actions
* [ ] Railway/Render PostgreSQL + App hosting

---

## 🛣️ Future Features

* [ ] JWT Auth with Refresh Tokens
* [ ] File Uploads for Assignments
* [ ] Admin Analytics Dashboard
* [ ] Email Notifications (grades, updates)
* [ ] GraphQL Layer (experimental)

---

## 👥 Contributors

* 🔥 **[Mamun](https://github.com/mamun700263)** — Lead Dev / Backend Sniper
* ⚙️ **[Trisha](https://github.com/TrishaPal2003)** — Contributor / DB & UI support

---

## 💼 Hire Me

I build clean, scalable, pressure-tested backend systems with production in mind. If you're hiring or collaborating:

📫 [mamun700263@gmail.com](mailto:mamun700263@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/md-abdullah-all-mamun/)
🌐 [GitHub](https://github.com/mamun700263)

---

> 🔥 If you're reading this, you're looking at a backend dev who *builds under fire* — clean APIs, clear structure, tested endpoints. No fluff. Just fire.


