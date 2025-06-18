# tasks/tests/test_labels.py
from django.test import TestCase
from django.urls import reverse
from labels.models import Label
from tasks.models import Task
from django.contrib.auth import get_user_model

User = get_user_model()

class LabelCRUDTest(TestCase):
    def setUp(self):
        self.label = Label.objects.create(name='Bug')
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_label_list(self):
        response = self.client.get(reverse('label-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bug')

    def test_label_create(self):
        response = self.client.post(reverse('label-create'), {'name': 'Feature'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Label.objects.filter(name='Feature').exists())

    def test_label_delete_with_tasks(self):
        task = Task.objects.create(title='Test', author=self.user)
        task.labels.add(self.label)
        response = self.client.post(reverse('label-delete', args=[self.label.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Label.objects.filter(id=self.label.id).exists())  # Метка не удалена