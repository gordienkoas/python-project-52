from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from task_manager_.models import Task, Label
from task_manager_.filters import TaskFilter

User = get_user_model()

class TaskFilterTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user1 = User.objects.create_user(username='user1', password='pass')
        self.user2 = User.objects.create_user(username='user2', password='pass')

        self.label1 = Label.objects.create(name='Bug')
        self.label2 = Label.objects.create(name='Feature')

        self.task1 = Task.objects.create(
            title='Task 1',
            description='Desc 1',
            status='new',
            author=self.user1,
            executor=self.user2,
        )
        self.task1.labels.add(self.label1)

        self.task2 = Task.objects.create(
            title='Task 2',
            description='Desc 2',
            status='done',
            author=self.user2,
            executor=self.user1,
        )
        self.task2.labels.add(self.label2)

        self.task3 = Task.objects.create(
            title='Task 3',
            description='Desc 3',
            status='in_progress',
            author=self.user1,
            executor=None,
        )
        # без меток

    def test_filter_by_status(self):
        data = {'status': 'new'}
        filter = TaskFilter(data=data, queryset=Task.objects.all())
        self.assertEqual(
            list(filter.qs.order_by('id')),
            list(Task.objects.filter(status='new').order_by('id'))
        )

    def test_filter_by_executor(self):
        data = {'executor': str(self.user1.id)}
        filter = TaskFilter(data=data, queryset=Task.objects.all())
        self.assertEqual(
            list(filter.qs.order_by('id')),
            list(Task.objects.filter(executor=self.user1).order_by('id'))
        )

    def test_filter_by_labels(self):
        data = {'labels': [self.label1.id]}
        filter = TaskFilter(data=data, queryset=Task.objects.all())
        self.assertEqual(
            list(filter.qs.order_by('id')),
            list(Task.objects.filter(labels=self.label1).order_by('id'))
        )

    def test_filter_by_author_true(self):
        # Симулируем запрос с автором user1 и фильтром author=True
        request = self.factory.get('/tasks/', {'author': 'on'})
        request.user = self.user1
        filter = TaskFilter(data={'author': True}, queryset=Task.objects.all(), request=request)
        self.assertEqual(
            list(filter.qs.order_by('id')),
            list(Task.objects.filter(author=self.user1).order_by('id'))
        )

    def test_filter_by_author_false(self):
        request = self.factory.get('/tasks/', {'author': ''})
        request.user = self.user1
        filter = TaskFilter(data={'author': False}, queryset=Task.objects.all(), request=request)
        self.assertEqual(
            list(filter.qs.order_by('id')),
            list(Task.objects.all().order_by('id'))
        )

