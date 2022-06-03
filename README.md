## Project: Our tools
Containerized (Docker) Django Rest Framework API serving hardware tools available (for a tool sharing app) in Postgres database.

Gunicorn production server
JWT token based authorizations

Permissions policy:
1. Must be authenticated to access info
2. Owner or ReadOnly

### Setup
To build and run the container use `docker compose up --build`

Run container with `docker compose up`
Disable container with `docker compose down`

### Tests

Manually tested:
- Log in / log out
- Mandatory authentication to access information
- CRUD operations subject to Owner or ReadOnly permissions
- Database persistence on docker volumes
- Detail view (by id)
- Create
- Update and Delete view
- Tokens view
- Token refresh view
