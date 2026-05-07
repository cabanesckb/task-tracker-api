# Task Tracker API

## Description
Task Tracker is a REST API built with Django and Django REST Framework.
It allows users to register, authenticate using JWT, and manage their
own tasks. Each user can only access and modify their own tasks.

## Tech Stack
- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT (SimpleJWT)

## Features
- User registration and JWT authentication
- Create, read, update, and delete tasks
- Each user can only access their own tasks

## Installation

1. Clone the repository
```bash
git clone https://github.com/cabanesckb/task-tracker-api
```

2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` and fill in your values
```bash
copy .env.example .env
```

5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Run the server
```bash
python manage.py runserver
```

## Environment Setup

Copy `.env.example` to `.env` and fill in your values:

```
SECRET_KEY=your_django_secret_key
DB_NAME=task_tracker
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
```

## API Endpoints

### Auth
| Method | URL | Description |
|--------|-----|-------------|
| POST | /api/register/ | Register a new user |
| POST | /api/token/ | Login and get tokens |
| POST | /api/token/refresh/ | Refresh access token |

### Tasks (requires Bearer token)
| Method | URL | Description |
|--------|-----|-------------|
| GET | /api/tasks/ | List your tasks |
| POST | /api/tasks/ | Create a new task |
| GET | /api/tasks/{id}/ | Get a single task |
| PUT | /api/tasks/{id}/ | Update a task |
| DELETE | /api/tasks/{id}/ | Delete a task |

## Usage

### Register
```json
POST /api/register/
{
    "username": "your_username",
    "password": "your_password"
}
```

### Login
```json
POST /api/token/
{
    "username": "your_username",
    "password": "your_password"
}
```

### Access Protected Endpoints
```
Authorization: Bearer your_access_token
```

## Running Tests
```bash
python manage.py test tasks
```