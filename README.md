# Hospital Management System

A Django application provides a robust platform for managing various aspects of hospital operations, aiming to streamline workflows and enhance patient care. 

## Features

- Patient Management: Add, view, edit, and delete patient records.
- Doctor Management: Add, view, edit, and delete doctor profiles.
- Appointment Management: Schedule, view, edit, and cancel appointments.
- Payment Management: Record and track patient payments.
- Room Allotment: Assign and manage hospital room allotments.
- User Authentication: Login and signup functionality for admins and staff members.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/hospital-management.git
```

2. Install the Requirements:

```bash
pip install -r requirements.txt
```

3. Then, make database migrations

```bash
python manage.py makemigrations
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Create a superuser account (for admin access):

```bash
python manage.py createsuperuser
```

6. Start the development server:

```bash
python manage.py runserver
```

The application should now be accessible at `http://127.0.0.1:8000/`.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

