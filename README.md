Got it! I've updated the `README.md` to reflect the new directory structure and the provided `.env.prod` example. Here's the revised version:

---

# Django HTMX CRUD Project with Docker

This is a CRUD (Create, Read, Update, Delete) application built with **Django**, **HTMX**, and **PostgreSQL**, containerized using **Docker Compose**. The project is designed to be easily deployable and scalable.

---

## Features

- **Django**: A high-level Python web framework for rapid development.
- **HTMX**: Lightweight library for adding dynamic behavior to your HTML without writing JavaScript.
- **PostgreSQL**: A powerful, open-source relational database.
- **Docker Compose**: Simplifies the setup and deployment of the application in isolated containers.

---

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## Getting Started

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 2. Set Up Environment Variables

1. Rename the `.env.example` file to `.env.prod`:
   ```bash
   cp .env.example .env.prod
   ```

2. Open `.env.prod` and fill in the required environment variables:
   ```plaintext
   # Django Settings
   API_KEY_EXCHANGE_RATE=your_api_key
   SECRET_KEY=your-secret-key
   DEBUG=0
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
   CSRF_TRUSTED_ORIGINS='http://127.0.0.1'

   # Database Settings
   SQL_ENGINE=django.db.backends.postgresql
   DATABASE=your_db_name
   SQL_USER=your_db_user
   SQL_PASSWORD=your_db_password
   SQL_HOST=db
   SQL_PORT=5432
   ```

---

### 3. Build and Run the Application

1. Build the Docker images:
   ```bash
   docker compose --env-file .env.prod -f docker-compose.prod.yml build
   ```

2. Start the containers in detached mode:
   ```bash
   docker compose --env-file .env.prod -f docker-compose.prod.yml up -d
   ```

3. Apply database migrations:
   ```bash
   docker compose --env-file .env.prod -f docker-compose.prod.yml exec web python manage.py migrate
   ```

4. (Optional) Create a superuser for the Django admin panel:
   ```bash
   docker compose --env-file .env.prod -f docker-compose.prod.yml exec web python manage.py createsuperuser
   ```

---

### 4. Access the Application

- **Django Application**: Open your browser and go to `http://localhost:8000`.
- **Admin Panel**: Access the Django admin panel at `http://localhost:8000/admin`.

---

## Project Structure

```
your-repo-name/
├── .env.example          # Example environment variables file
├── docker-compose.prod.yml  # Docker Compose configuration for production
├── Dockerfile            # Dockerfile for the Django application
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
├── app/                  # Django application code
│   ├── models.py         # Database models
│   ├── views.py          # Application views
│   ├── templates/        # HTML templates
│   └── ...
└── ...
```

---

## Docker Compose Configuration

The `docker-compose.prod.yml` file defines the following services:

- **web**: The Django application.
- **db**: PostgreSQL database.
- **nginx**: Reverse proxy for serving static files and handling requests.

---

## Environment Variables

| Variable                | Description                          | Example Value          |
|-------------------------|--------------------------------------|------------------------|
| `API_KEY_EXCHANGE_RATE` | API key for exchange rate service    | `your_api_key`         |
| `SECRET_KEY`            | Django secret key                   | `your-secret-key`      |
| `DEBUG`                 | Enable/disable debug mode           | `0` (False) or `1` (True) |
| `DJANGO_ALLOWED_HOSTS`  | Allowed hosts for Django            | `localhost,127.0.0.1`  |
| `CSRF_TRUSTED_ORIGINS`  | Trusted origins for CSRF            | `http://127.0.0.1`     |
| `SQL_ENGINE`            | Database engine                     | `django.db.backends.postgresql` |
| `DATABASE`              | PostgreSQL database name            | `your_db_name`         |
| `SQL_USER`              | PostgreSQL username                 | `your_db_user`         |
| `SQL_PASSWORD`          | PostgreSQL password                 | `your_db_password`     |
| `SQL_HOST`              | PostgreSQL host                     | `db`                   |
| `SQL_PORT`              | PostgreSQL port                     | `5432`                 |

---

## Stopping the Application

To stop the running containers, use:

```bash
docker compose --env-file .env.prod -f docker-compose.prod.yml down
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [HTMX](https://htmx.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)

---

Enjoy building with Django, HTMX, and Docker! 🚀

---

This updated `README.md` now reflects the new directory structure and the provided `.env.prod` example. Let me know if you need further adjustments! 😊
