# Task Tracker API

## Description
Task Tracker is a REST API built with Django and Django REST Framework. 
It allows users to register, authenticate using JWT, and manage their 
own tasks. Each user can only access and modify their own tasks.

## Tech Stack
Python, Django, Django Rest Framework, JWT

## Features
Register, Login, List Tasks, Update task, and Delete Task


## Installation
1. Clone the repository
   git clone https://github.com/your_username/task-tracker-api

2. Create and activate virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Configure your database in config/settings.py

5. Run migrations
   python manage.py makemigrations
   python manage.py migrate

6. Run the server
   python manage.py runserver

## Environment Setup
you need to edit database based on your database setting
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'task_tracker',
        'USER': 'postgres',
        'PASSWORD': 'your_postgres_password',
        'host': 'localhost',
        'port': '5432',
    }
}

## API Endpoints

### Auth
| Method | URL | Description |
|--------|-----|-------------|
| POST | api/register/ | Register a new user |
| POST | api/token/ | Login and get access + refresh token |
| POST | api/token/refresh/ | Get new access token |

### Tasks (requires Bearer token)
| Method | URL | Description |
|--------|-----|-------------|
| GET | api/tasks/ | List all your tasks |
| POST | api/tasks/ | Create a new task |
| GET | api/tasks/{id}/ | Get a single task |
| PUT | api/tasks/{id}/ | Update a task |
| DELETE | api/tasks/{id}/ | Delete a task |

## Usage

### Register
POST api/register/
{
    "username": "your_username",
    "password": "your_password"
}

### Login
POST api/token/
{
    "username": "your_username",
    "password": "your_password"
}
→ returns access and refresh token

### Access protected endpoints
Add this header to every request:
Authorization: Bearer your_access_token

## Running Tests
python manage.py test tasks