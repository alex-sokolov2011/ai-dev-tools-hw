from django.test import TestCase, Client
from django.urls import reverse
from datetime import date, timedelta
from .models import Todo


class TodoModelTest(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(
            title="Test TODO",
            description="Test description",
            due_date=date.today() + timedelta(days=7),
            is_resolved=False
        )

    def test_todo_creation(self):
        self.assertEqual(self.todo.title, "Test TODO")
        self.assertEqual(self.todo.description, "Test description")
        self.assertFalse(self.todo.is_resolved)
        self.assertIsNotNone(self.todo.created_at)
        self.assertIsNotNone(self.todo.updated_at)

    def test_todo_str_method(self):
        self.assertEqual(str(self.todo), "Test TODO")

    def test_todo_optional_fields(self):
        todo = Todo.objects.create(title="Minimal TODO")
        self.assertEqual(todo.description, "")
        self.assertIsNone(todo.due_date)
        self.assertFalse(todo.is_resolved)

    def test_todo_default_is_resolved(self):
        todo = Todo.objects.create(title="New TODO")
        self.assertFalse(todo.is_resolved)

    def test_todo_due_date(self):
        due_date = date.today() + timedelta(days=7)
        self.assertEqual(self.todo.due_date, due_date)


class TodoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.todo1 = Todo.objects.create(
            title="First TODO",
            description="First description",
            is_resolved=False
        )
        self.todo2 = Todo.objects.create(
            title="Second TODO",
            description="Second description",
            due_date=date.today() + timedelta(days=3),
            is_resolved=True
        )

    def test_home_view_get(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todos/home.html')
        self.assertContains(response, "First TODO")
        self.assertContains(response, "Second TODO")

    def test_home_view_displays_all_todos(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(len(response.context['todos']), 2)

    def test_create_todo_view_get(self):
        response = self.client.get(reverse('create_todo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todos/todo_form.html')
        self.assertContains(response, "Create TODO")

    def test_create_todo_view_post_valid(self):
        data = {
            'title': 'New TODO',
            'description': 'New description',
            'due_date': (date.today() + timedelta(days=5)).isoformat(),
            'is_resolved': False
        }
        response = self.client.post(reverse('create_todo'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Todo.objects.filter(title='New TODO').exists())
        new_todo = Todo.objects.get(title='New TODO')
        self.assertEqual(new_todo.description, 'New description')

    def test_create_todo_view_post_invalid(self):
        data = {'description': 'No title'}
        response = self.client.post(reverse('create_todo'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Todo.objects.filter(description='No title').exists())

    def test_edit_todo_view_get(self):
        response = self.client.get(reverse('edit_todo', args=[self.todo1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todos/todo_form.html')
        self.assertContains(response, "First TODO")

    def test_edit_todo_view_post_valid(self):
        data = {
            'title': 'Updated TODO',
            'description': 'Updated description',
            'is_resolved': True
        }
        response = self.client.post(reverse('edit_todo', args=[self.todo1.id]), data)
        self.assertEqual(response.status_code, 302)
        self.todo1.refresh_from_db()
        self.assertEqual(self.todo1.title, 'Updated TODO')
        self.assertEqual(self.todo1.description, 'Updated description')
        self.assertTrue(self.todo1.is_resolved)

    def test_edit_todo_view_not_found(self):
        response = self.client.get(reverse('edit_todo', args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_delete_todo_view(self):
        todo_id = self.todo1.id
        response = self.client.post(reverse('delete_todo', args=[todo_id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Todo.objects.filter(id=todo_id).exists())

    def test_delete_todo_view_not_found(self):
        response = self.client.post(reverse('delete_todo', args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_toggle_resolved_view_to_resolved(self):
        self.assertFalse(self.todo1.is_resolved)
        response = self.client.post(reverse('toggle_resolved', args=[self.todo1.id]))
        self.assertEqual(response.status_code, 302)
        self.todo1.refresh_from_db()
        self.assertTrue(self.todo1.is_resolved)

    def test_toggle_resolved_view_to_unresolved(self):
        self.assertTrue(self.todo2.is_resolved)
        response = self.client.post(reverse('toggle_resolved', args=[self.todo2.id]))
        self.assertEqual(response.status_code, 302)
        self.todo2.refresh_from_db()
        self.assertFalse(self.todo2.is_resolved)

    def test_toggle_resolved_view_not_found(self):
        response = self.client.post(reverse('toggle_resolved', args=[9999]))
        self.assertEqual(response.status_code, 404)


class TodoIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_full_todo_lifecycle(self):
        # Create a TODO
        create_data = {
            'title': 'Integration Test TODO',
            'description': 'Testing full lifecycle',
            'due_date': (date.today() + timedelta(days=10)).isoformat(),
            'is_resolved': False
        }
        response = self.client.post(reverse('create_todo'), create_data)
        self.assertEqual(response.status_code, 302)
        
        # Verify TODO exists
        todo = Todo.objects.get(title='Integration Test TODO')
        self.assertIsNotNone(todo)
        
        # Edit the TODO
        edit_data = {
            'title': 'Updated Integration TODO',
            'description': 'Updated description',
            'is_resolved': False
        }
        response = self.client.post(reverse('edit_todo', args=[todo.id]), edit_data)
        self.assertEqual(response.status_code, 302)
        todo.refresh_from_db()
        self.assertEqual(todo.title, 'Updated Integration TODO')
        
        # Toggle resolved
        response = self.client.post(reverse('toggle_resolved', args=[todo.id]))
        self.assertEqual(response.status_code, 302)
        todo.refresh_from_db()
        self.assertTrue(todo.is_resolved)
        
        # Delete the TODO
        response = self.client.post(reverse('delete_todo', args=[todo.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Todo.objects.filter(id=todo.id).exists())

    def test_empty_todo_list(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No TODOs yet")
