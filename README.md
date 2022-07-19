# Test task
## Student and section API
## Django, Django REST API,

## Installation

1. python3 -m venv venv / or create your own Virtual Environment
2. activate the venv
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py runserver

or

1. poetry install
2. poetry run manage.py migrate
3. poetry run manage.py runserver

## Models

* `Student` - This model represents a dog in the app.

	Fields:

	* `name`
	* `is_teacher`
	* `is_student`

* `Secion` -  This model represents a link between a user an a dog

	Fields:

	* `name`
	* `students`, list of students

    Memberships: (through table for many to many relationship between student and section)
    * `student`
    * `section`
    * `date_joined`

## Routes

The following routes are expected by the JavaScript application.

* To get the next lists of students or sections

	* `/api/v1/sections/`
	* `/api/v1/sections/<pk>/`
	* `/api/v1/students/`
	* `/api/v1/students/<pk>/`, update student only, delete admin only

* To auth
	* `/api/v1/auth/users/`, register new user
	* `/auth/token/login/`, get token
