# LAB - Class 32

## Project: Our tools
Containerized (Docker) Django Rest Framework API with Permissions app showing tools available (for a tool sharing app)

### Setup
To build container use `docker compose up --build`

Run container with `docker compose up`
Inside the container use `python manage.py runserver`, to run app API.


### Tests
Use `python manage.py test`, to run tests.

Current unit tests:
- Model -model fields match entered data
- List view
- Detail view (by id)
- Create
- Update
- Delete
- Authentication required
