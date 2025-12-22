# Django TODO Application

A fully functional TODO application built with Django, featuring create, read, update, and delete (CRUD) operations for managing tasks.

## Features

- Create new TODOs with title, description, and due date
- Edit existing TODOs
- Delete TODOs with confirmation
- Mark TODOs as resolved/unresolved
- Beautiful Bootstrap-based UI
- Due date tracking with visual indicators
- Full test coverage (20 tests)
- SQLite database (default Django database)

## Project Structure

```
01-todo/
├── manage.py
├── todoproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── todos/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── templates/
│   │   └── todos/
│   │       ├── base.html
│   │       ├── home.html
│   │       └── todo_form.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
└── README.md
```

## Requirements

- Python 3.x
- Django 5.2.9 or later

## Installation and Setup

### 1. Install Django

```bash
pip install django
# OR using uv:
uv pip install django
```

### 2. Navigate to Project Directory

```bash
cd 01-todo
```

### 3. Run Migrations

Create and apply database migrations:

```bash
python manage.py migrate
```

If you encounter database lock issues on WSL/Windows, try:
```bash
rm -f db.sqlite3
python manage.py migrate
```

### 4. (Optional) Create a Superuser

To access the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 5. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

### Creating a TODO

1. Click the "+ New TODO" button in the navigation bar
2. Fill in the TODO details:
   - **Title** (required): A short description of the task
   - **Description** (optional): Additional details about the task
   - **Due Date** (optional): When the task should be completed
   - **Mark as Resolved** (checkbox): Whether the task is completed
3. Click "Create TODO" to save

### Viewing TODOs

The home page displays all TODOs with:
- Title and description
- Due date (if set)
- Status badge (Resolved/Pending)
- Creation date
- Action buttons

### Editing a TODO

1. Click the "Edit" button on any TODO
2. Modify the fields as needed
3. Click "Edit TODO" to save changes

### Marking as Resolved/Unresolved

Click the "Mark Resolved" or "Mark Pending" button to toggle the status.

### Deleting a TODO

1. Click the "Delete" button on any TODO
2. Confirm the deletion in the popup dialog

## Running Tests

The project includes comprehensive test coverage:

```bash
python manage.py test
```

For verbose output:

```bash
python manage.py test --verbosity 2
```

### Test Coverage

- **Model Tests** (5 tests): Test TODO model creation, fields, and methods
- **View Tests** (13 tests): Test all CRUD operations and edge cases
- **Integration Tests** (2 tests): Test complete workflows

All 20 tests should pass successfully.

## Models

### Todo Model

| Field | Type | Description |
|-------|------|-------------|
| title | CharField(200) | TODO title (required) |
| description | TextField | Detailed description (optional) |
| due_date | DateField | Due date (optional) |
| is_resolved | BooleanField | Completion status (default: False) |
| created_at | DateTimeField | Auto-generated creation timestamp |
| updated_at | DateTimeField | Auto-updated modification timestamp |

## URLs

| URL Pattern | View | Name | Description |
|-------------|------|------|-------------|
| `/` | home | home | List all TODOs |
| `/create/` | create_todo | create_todo | Create new TODO |
| `/edit/<id>/` | edit_todo | edit_todo | Edit existing TODO |
| `/delete/<id>/` | delete_todo | delete_todo | Delete TODO |
| `/toggle/<id>/` | toggle_resolved | toggle_resolved | Toggle resolved status |

## Technologies Used

- **Backend**: Django 5.2.9
- **Database**: SQLite3
- **Frontend**: HTML5, Bootstrap 5.3.0
- **Forms**: Django ModelForm
- **Messages**: Django messages framework

## Features Implemented

- Full CRUD functionality
- Form validation using Django forms
- User feedback with Django messages
- Responsive design with Bootstrap
- CSRF protection
- Confirmation dialogs for destructive actions
- Date formatting and display
- Visual status indicators
- Comprehensive test suite

## Troubleshooting

### Database Locked Error

If you encounter a "database is locked" error on WSL/Windows systems:

1. Stop any running Django development server
2. Delete the database file: `rm -f db.sqlite3`
3. Run migrations again: `python manage.py migrate`

### Port Already in Use

If port 8000 is already in use, run the server on a different port:

```bash
python manage.py runserver 8001
```

### Static Files Not Loading

Run the collectstatic command:

```bash
python manage.py collectstatic
```

## License

This project is created for educational purposes as part of a course homework assignment.

## Author

Course Homework Assignment - Django TODO Application
