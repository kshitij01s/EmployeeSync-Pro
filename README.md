# EmployeeSync Pro  
**Enterprise-Grade Employee Management System | Full-Stack Django**

Live Demo: http://127.0.0.1:8000 (Run locally)  
GitHub: https://github.com/kshitij01s/EmployeeSync-Pro

![Project Preview](https://github.com/kshitij01s/EmployeeSync-Pro/blob/main/screenshots/homepage.png?raw=true)

### The Most Complete & Beautiful Employee Management System Built with Django

## Features
- Full REST API with proper validation & error codes
- API Key Authentication (`X-API-Key` header)
- Direct Stored Procedure Integration (`/stored-proc/`)
- Lightning-fast Web Dashboard with Pagination
- Glassmorphism Futuristic Homepage with Live Status
- Fully Responsive Design (Mobile + Desktop)
- Professional Django Admin Panel
- Clean, Production-Ready Codebase

## Tech Stack
- Django 5.x (Python)
- Bootstrap 5 + Bootstrap Icons
- Custom CSS (Glassmorphism, Animations, Orbitron Font)
- SQLite (default) – easily switch to PostgreSQL/SQL Server

## Project Structure
EmployeeSync-Pro/
├── apiapp/
│   ├── models.py          → Employee model
│   ├── views.py           → All API + Web Dashboard logic
│   ├── admin.py           → Beautiful admin panel
│   ├── utils/
│   │   ├── call_proc.py        → Call SQL stored procedures
│   │   └── validate_api_key.py → API Key security
│   └── templates/app/employee_app.html → Web dashboard
├── apiproject/urls.py     → Stunning homepage + routing
└── static/ & templates/   → Styling & HTML


## API Endpoints
| Endpoint               | Method     | Description                     | Auth Required |
|------------------------|------------|---------------------------------|----------------|
| `/`                    | GET        | Futuristic Homepage             | No             |
| `/app/`                | GET        | Web Dashboard (Paginated)       | No             |
| `/admin/`              | GET        | Django Admin                    | Login          |
| `/employee/`           | GET        | List all employees              | API Key        |
| `/employee/`           | POST       | Create employee                 | API Key        |
| `/employee/<id>/`      | GET/PUT/DELETE | Single employee             | API Key        |
| `/stored-proc/`        | POST       | Call any allowed stored procedure | API Key      |

## Quick Start
```bash
git clone https://github.com/kshitij01s/EmployeeSync-Pro.git
cd EmployeeSync-Pro
python -m venv venv
venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py runserver

Then open: http://127.0.0.1:8000
API Testing Example (Postman/curl)
   curl -X GET http://127.0.0.1:8000/employee/ \
  -H "X-API-Key: your-secret-key-here"

Screenshots
Homepage
<img width="1897" height="884" alt="image" src="https://github.com/user-attachments/assets/1b1cba54-42c9-4374-8695-b6034212523f" />

Web Dashboard
<img width="1469" height="415" alt="image" src="https://github.com/user-attachments/assets/8e5b8987-cac9-4a86-ab60-5778c2a2e775" />

Admin Panel
<img width="1903" height="873" alt="image" src="https://github.com/user-attachments/assets/11aad770-a2c4-48d1-82f9-14692075c1e6" />



