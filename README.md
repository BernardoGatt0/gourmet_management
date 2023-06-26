# API in Django with Django REST Framework - Gourmet Management

![Badge License: MIT](https://img.shields.io/github/license/darlangui/e-commerce?style=for-the-badge)

## Project Description

This is a Django API developed using Django REST Framework. The API provides endpoints for creating, reading, updating, and deleting resources, following the principles of the REST architecture.

## Prerequisites

Make sure you have the following requirements installed on your local machine:

  - Python (version 3.8).
  - Django (version 4.2 or higher).
  - Django REST Framework (version 3.14 or higher).

## Environment Setup

1. Clone this repository to your local machine:

  ```bash
  git clone https://github.com/BernardoGatt0/gourmet_management.git
  ```

2. Navigate to the project directory:

  ```bash
  cd gourmet_management
  ```

3. Create and activate a virtual environment (optional but recommended):

  ```bash
  python -m venv env
  source env/bin/activate
  ```

4. Install the dependencies:

 ```bash
  pip install -r requirements.txt
 ```

5. Apply the database migrations:

 ```bash
  python manage.py migrate
 ```

## Running the Server

To start the development server, run the following command:
  
  ```bash
  python manage.py runserver
  ```

Access the API in your browser at http://localhost:8000/ or through an API client such as Postman.

## Available Endpoints

- `/cadapio` : GET (list all resources) and POST (create a new resource).
- `/mesa` : GET (list all resources) and POST (create a new resource).
- `/comanda` : GET (list all resources) and POST (create a new resource).
- `/pedido` : GET (list all resources) and POST (create a new resource).
- `/media/{id}` : GET (retrieve a resource by ID).

## Authentication and Permissions

Authentication and permissions have been configured to provide secure access to the API. You can modify the authentication and permission settings in the settings.py file according to your needs.

## License

This project is licensed under the MIT License.
