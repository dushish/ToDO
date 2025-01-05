from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task

class ToDoAppTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.task = Task.objects.create(user=self.user, title="Test Task", description="Test Description")

    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'securepassword',
            'password2': 'securepassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_login(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password'})
        self.assertEqual(response.status_code, 302)

    def test_create_task(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('create_task'), {
            'title': 'New Task',
            'description': 'New Task Description'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title="New Task").exists())

    def test_task_restriction(self):
        new_user = User.objects.create_user(username="otheruser", password="password")
        self.client.login(username='otheruser', password='password')
        response = self.client.get(reverse('edit_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 403)
