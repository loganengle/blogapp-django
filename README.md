# MyBlog

MyBlog is a Django-based blogging site with Docker support. This project allows users to create, view, and search blog posts, and it includes Docker setup for easy deployment.

## Prerequisites

Before you start, make sure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Poetry](https://python-poetry.org/docs/#installation)

## Getting Started

Follow these steps to set up and run the project:

### 1. Clone the Repository

```shell
git clone https://github.com/loganengle/blogapp_django.git
cd blogapp_django
```

### 2. Build and Start Docker Containers

```shell
docker-compose up --build
```

### 3. Create a Superuser

```shell
docker-compose exec web python manage.py createsuperuser
```

### 4. Load Dummy Data

```shell
docker-compose exec web python manage.py loaddata fixtures/posts.json
```

### 5. Access the Application

Open your browser and navigate to http://localhost:8000 to view the blog.
Navigate to http://localhost:8000/admin to log in and manage blog posts and users.
