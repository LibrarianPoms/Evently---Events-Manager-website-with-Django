# Evently — Events Manager Website with Django

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Django-5.x-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
</p>

Evently is a web application built with **Django** designed to simplify event creation, scheduling, and management. It allows organizers to publish and manage events while attendees can browse upcoming events with full details including date, time, location, duration, and capacity.

---

## Features

- **Event Management**: Create, update, view, and delete events.
- **Detailed Event Attributes**:
  - Title & description
  - Date, start time, and duration
  - Location details
  - Attendee capacity tracking
  - Event cover image upload
- **User Authentication & Roles**:
  - Registration and login workflows
  - Role-based permissions (organizer controls)
- **Django Administration**: Built-in Django admin interface for managing users, permissions, and events.

---

## Project Structure

```text
event_project/
├── event/                      # Core event application
│   ├── migrations/             # Database migrations
│   ├── templates/              # HTML templates (forms, auth, details)
│   ├── admin.py                # Admin site configuration
│   ├── apps.py                 # App configuration
│   ├── forms.py                # Django forms (EventForm, CustomUserCreationForm)
│   ├── models.py               # Database models (Event, User associations)
│   ├── tests.py                # Unit and integration tests
│   └── views.py                # View handlers & business logic
├── event_project/              # Project settings & configuration
│   ├── asgi.py                 # ASGI entrypoint
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Global URL routing
│   └── wsgi.py                 # WSGI entrypoint
├── manage.py                   # Django CLI management script
├── .gitignore                  # Git ignore rules
└── README.md                   # Project documentation
```

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- `pip` (Python package installer)
- `git`

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/LibrarianPoms/Evently---Events-Manager-website-with-Django.git
   cd Evently---Events-Manager-website-with-Django
   ```

2. **Create and activate a virtual environment**:
   - **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **macOS / Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install django pillow
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (for admin access)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and navigate to:
   - Application: `http://127.0.0.1:8000/`
   - Admin Panel: `http://127.0.0.1:8000/admin/`

---

## Routes & Endpoints

| URL Path | View | Description |
| :--- | :--- | :--- |
| `/` | `event_list` | Browse all available events |
| `/event/<id>/` | `event_detail` | Detailed view of a single event |
| `/event/create/` | `create_event` | Create a new event (Organizers) |
| `/event/<id>/edit/` | `update_event` | Edit an existing event |
| `/event/<id>/delete/` | `delete_event` | Delete an event |
| `/admin/` | Django Admin | Admin panel for system management |

---

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/LibrarianPoms/Evently---Events-Manager-website-with-Django/issues).

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
