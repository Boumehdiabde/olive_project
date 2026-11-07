# 🌳 Olive Project - Olive Cultivation Management System

A comprehensive Django-based web application for managing olive groves, tracking harvests, and maintaining cultivation records.

## 📋 Features

- **Grove Management**: Create and manage multiple olive groves with detailed information
- **Harvest Tracking**: Record and track harvests with quality grades and oil yield
- **Maintenance Logging**: Keep track of maintenance tasks, pruning, irrigation, pest control, and more
- **Dashboard Statistics**: View real-time statistics about your olive groves
- **Admin Panel**: Full-featured Django admin interface for data management
- **REST API**: JSON API endpoints for programmatic access
- **Web Interface**: Beautiful, responsive web pages for easy navigation

## 🛠️ Tech Stack

- **Backend**: Django 6.0.4
- **API**: Django REST Framework 3.14.0
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: HTML5, CSS3
- **Server**: Gunicorn

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip
- virtualenv (optional but recommended)

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/Boumehdiabde/olive_project.git
cd olive_project
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Apply migrations**
```bash
python manage.py migrate
```

5. **Create superuser (admin account)**
```bash
python manage.py createsuperuser
```

6. **Run development server**
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## 🌐 Accessing the Application

- **Home Dashboard**: `http://localhost:8000/`
- **Groves List**: `http://localhost:8000/groves/`
- **Admin Panel**: `http://localhost:8000/admin/` (use superuser credentials)
- **API Endpoints**:
  - Dashboard Stats: `http://localhost:8000/api/stats/`
  - All Groves: `http://localhost:8000/api/groves/`
  - Grove Details: `http://localhost:8000/api/groves/{id}/`
  - Harvests: `http://localhost:8000/api/harvests/`
  - Maintenance Logs: `http://localhost:8000/api/maintenance/`

## 📊 Models

### Grove
- Name, location, variety (Koroneiki, Arbequina, Picual, Frantoio)
- Tree count, area in hectares, planting year
- Irrigation type, soil type, status
- Notes and image URL
- Relationships: Multiple harvests and maintenance logs

### Harvest
- Grove reference
- Harvest date, quantity (kg)
- Quality grade, oil yield (%)
- Notes

### MaintenanceLog
- Grove reference
- Task type (Pruning, Irrigation, Fertilization, Pest Control, Disease Treatment)
- Date, description, cost
- Completion status

## 🔧 Available Management Commands

```bash
# Create database tables
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Run tests
python manage.py test

# Create static files
python manage.py collectstatic
```

## 📝 API Usage Examples

### Get Dashboard Statistics
```bash
curl http://localhost:8000/api/stats/
```

### Get All Groves
```bash
curl http://localhost:8000/api/groves/
```

### Get Specific Grove
```bash
curl http://localhost:8000/api/groves/1/
```

## 🚀 Deployment

### Production Checklist
1. Set `DEBUG = False` in settings.py
2. Add your domain to `ALLOWED_HOSTS`
3. Use strong `SECRET_KEY`
4. Switch to PostgreSQL database
5. Configure environment variables (.env file)
6. Run `python manage.py collectstatic`
7. Use Gunicorn with Nginx reverse proxy

### Example Gunicorn Command
```bash
gunicorn olive_project.wsgi:application --bind 0.0.0.0:8000 --workers 4
```

## 📚 Project Structure

```
olive_project/
├── core/                      # Main app
│   ├── models.py             # Database models
│   ├── views.py              # View functions
│   ├── serializers.py        # DRF serializers
│   ├── admin.py              # Admin configuration
│   └── migrations/           # Database migrations
├── olive_project/            # Project settings
│   ├── settings.py           # Django settings
│   ├── urls.py               # URL routing
│   ├── wsgi.py               # WSGI config
│   └── asgi.py               # ASGI config
├── templates/                # HTML templates
│   └── core/
│       ├── base.html         # Base template
│       ├── home.html         # Dashboard
│       ├── groves_list.html  # Groves listing
│       ├── grove_detail.html # Grove details
│       └── 404.html          # 404 page
├── manage.py                 # Django management script
├── requirements.txt          # Project dependencies
└── README.md                 # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Boumehdiabde** - [GitHub Profile](https://github.com/Boumehdiabde)

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Happy Olive Cultivation! 🌳🫒**
