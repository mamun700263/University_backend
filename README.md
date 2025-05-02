# 🎓 CCN UST - University Management System

A centralized, role-based University Management System built with Django to streamline academic operations for students, teachers, and administrators at CCN UST.

## 🔥 Features (MVP)

- ✅ Role-based login system (Admin, Teacher, Student)
- ✅ Course creation and assignment
- ✅ Student enrollment management
- ✅ Attendance tracking per course
- ✅ Grade/result management
- ✅ Announcement/notice system
- ✅ Individual dashboards for each role

## ⚙️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript (Plan to upgrade to React later)
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **Authentication**: Django Auth (with custom user roles)
- **Deployment**: *(to be added)*

## 🧑‍💻 Team

- **[Md Abdullah Al Mamun](https://github.com/mamun700263)** — Backend Dev / Project Lead  
- **[Trisha pal](https://github.com/trishapal2003)** — Django Developer (Views, Templates, Forms)  
- **[Nahian safa](https://github.com/Nahian07)** — Frontend Developer (HTML, CSS, JS)

## 🚀 Getting Started

Clone the repo and set up the virtual environment:  

```bash
git clone https://github.com/yourusername/ccnust-management.git
cd ccnust-management

python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


---

apps:
Accounts
    - there are all the possible accounts models and everything related to accounts (student, teacher,stuf, authority)
Departments
    - it handels the departments structure
university-
    - this is app that will be responsible for maintaing the date erlated to ccn university
