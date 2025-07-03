
# 🌦️ Weather API - Django REST Framework

This is a backend Weather API built using **Django** and **Django REST Framework**. It allows you to:

- Add and list cities 🌍  
- Log weather data for cities 🌡️  
- Let users save favorite cities ⭐  
- Retrieve saved cities and search cities 🔍  

The project uses clean, modular design with proper serializers, views, and admin setup.

---

## 🚀 Features

- ✅ City CRUD: Add and list cities with name, country, and description
- ✅ Weather Logging: Log weather with temperature, humidity, and timestamp
- ✅ Saved Cities: Authenticated users can save cities
- ✅ Admin Support: All models visible and searchable in Django admin
- ✅ Search Support: City search by name (partial match)
- ✅ Formatted timestamps and readable outputs
- ✅ Modular code using class-based generic views

---

## 🧱 Tech Stack

| Layer          | Technology                     |
|----------------|--------------------------------|
| Language       | Python                         |
| Framework      | Django, Django REST Framework  |
| Database       | SQLite (dev), PostgreSQL-ready |
| Auth           | Django User Model              |
| Dev Tools      | Postman, Git, VS Code          |

---

## 📁 API Endpoints

| Method | Endpoint                 | Description                         |
|--------|--------------------------|-------------------------------------|
| POST   | `/api/city-add/`         | Add a new city                      |
| GET    | `/api/cities/`           | List all cities                     |
| GET    | `/api/search-city/?name=udg` | Search cities by name (partial) |
| POST   | `/api/weather-add/`      | Add weather data to a city          |
| GET    | `/api/weathers/`         | List all weather entries            |
| POST   | `/api/saved-city-add/`   | Save a city for a user              |
| GET    | `/api/saved-cities/`     | List saved cities                   |
| GET    | `/api/users/`            | List users                          |

---

## 🧪 Testing API

Use **Postman** or **cURL** to test the endpoints.  
Sample request to add a city:

```json
POST /api/city-add/
{
  "name": "Pune",
  "country": "IN",
  "description": "Cultural City"
}
```

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/your-username/weather-api.git
cd weather-api

# Create and activate virtual environment
python -m venv venv
source venv\Scripts\activate  # Windows

# Install requirements
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (for admin panel)
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/admin` for the admin panel.

---

## 🙋‍♀️ About Me

I’m a backend developer focusing on **Python/Django API development**, building real-world backend projects like this to demonstrate skills and help businesses connect data with users efficiently.

> Reach out for collaborations, freelancing, or feedback!

---

## 📌 To Do Next

- 🔐 Add JWT authentication
- 🌍 Integrate with OpenWeatherMap live API
- 📦 Dockerize the project
- 📈 Add Swagger/OpenAPI documentation

---

## 📄 License

This project is for educational and portfolio use.
