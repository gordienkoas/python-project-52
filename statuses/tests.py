from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth import get_user_model
from statuses.models import Status

class StatusUpdateTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='12345')
        self.client.force_login(self.user)
        self.status = Status.objects.create(name='Initial Status')

    def test_status_update(self):
        url = reverse('status-update', args=[self.status.id])
        data = {'name': 'Обновлённый статус'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # редирект

        # Следующий запрос — страница списка, куда редиректит
        response = self.client.get(reverse('status-list'))
        messages = list(get_messages(response.wsgi_request))

        print('Сообщения:', [str(m) for m in messages])  # Для отладки

        self.assertTrue(any('Статус успешно обновлен.' in str(m) for m in messages))