from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task

# Create your tests here.
class RegisterTestCase(TestCase):
    
    def setUp(self):
        self.client = APIClient()
    
    def test_register_valid_data(self):
        response = self.client.post('/api/register/', {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 201)
    
    def test_register_invalid_data(self):
        response = self.client.post('/api/register/', {
            'username': 'testuser',
        })
        self.assertEqual(response.status_code, 400)

class TaskListTestCase(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.client.force_authenticate(user=self.user)
    
    def test_get_task(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)
    
    def test_post_valid_task(self):
        response = self.client.post('/api/tasks/', {
            'description': 'tesk task',
            'status': 'todo'
        })
        self.assertEqual(response.status_code, 201)
    
    def test_post_invalid_task(self):
        response = self.client.post('/api/tasks/', {
            'description': 'tesk task',
            'status': 'notvalid'
        })
        self.assertEqual(response.status_code, 400)

class TaskDetailTestCase(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.client.force_authenticate(user=self.user)
        
        self.task = Task.objects.create(
            user=self.user,
            description='Test task',
            status='todo'
        )
    
    def test_get_task_detail(self):
        response = self.client.get(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, 200)
    
    def test_put_task_detail(self):
        response = self.client.put(f'/api/tasks/{self.task.id}/', {
            'description': 'new test task',
            'status': 'done',
        })
        self.assertEqual(response.status_code, 200)
    
    def test_delete_task_detail(self):
        response = self.client.delete(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, 204)
    
    def test_cannot_get_other_user_task(self):
        other_user = User.objects.create_user(
            username='otheruser',
            password='testpass'
        )
        
        other_task = Task.objects.create(
            user=other_user,
            description='Other users task',
            status='todo'
        )
        
        response = self.client.get(f'/api/tasks/{other_task.id}/')
        self.assertEqual(response.status_code, 404)


class AuthTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )

    def test_login_valid_credentials(self):
        response = self.client.post('/api/token/', {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 200)

    def test_login_invalid_credentials(self):
        response = self.client.post('/api/token/', {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 401)