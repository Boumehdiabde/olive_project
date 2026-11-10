# Olive Project - Olive Cultivation Management

A Django application for managing olive groves, tracking harvests, and recording maintenance.

## Features

- Grove records, variety/status filtering, and grove detail pages
- Harvest and maintenance history for each grove
- Dashboard totals and REST API endpoints
- Django admin for managing all records

## Requirements

- Python 3.10 or newer
- pip

## Run locally

```bash
git clone https://github.com/Boumehdiabde/olive_project.git
cd olive_project
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/>. Create an admin account with `python manage.py createsuperuser` and visit `/admin/` to manage records.

## API

- `GET /api/stats/` — grove, tree, area, and harvest totals
- `/api/groves/` — create/list/update/delete groves
- `/api/harvests/` — create/list/update/delete harvest records (include a `grove` ID)
- `/api/maintenance/` — create/list/update/delete maintenance records (include a `grove` ID)

## Configuration

For deployment, set `DJANGO_SECRET_KEY` to a unique secret, set `DJANGO_DEBUG=false`, and set `DJANGO_ALLOWED_HOSTS` to a comma-separated list of your domain names. The built-in SQLite database is intended for local development; configure a production database before deploying.

## Tests

```bash
python manage.py test
python manage.py check
```
