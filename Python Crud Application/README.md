# Python CRUD Application

A production-ready CRUD (Create, Read, Update, Delete) application built with FastAPI, SQLAlchemy, and PostgreSQL. This project demonstrates best practices for building scalable REST APIs with proper data validation and database management.

## Project Overview

This application showcases a complete backend implementation with a real PostgreSQL database, object-relational mapping (ORM), data validation, and containerization. It serves as a reference for building robust Python applications that handle database operations efficiently.

## Technology Stack

### FastAPI
FastAPI is a modern Python web framework for building APIs. It provides automatic request/response validation, interactive API documentation, and high performance. FastAPI makes it easy to create RESTful endpoints and handles data serialization automatically.

### SQLAlchemy
SQLAlchemy is an Object-Relational Mapping (ORM) library that bridges the gap between Python objects and database tables. Instead of writing raw SQL queries, SQLAlchemy lets you work with database records as Python objects. This makes code more maintainable, safer, and easier to refactor.

### PostgreSQL
PostgreSQL is a powerful, open-source relational database system. It provides ACID compliance, complex queries, and reliable data storage. PostgreSQL ensures data integrity and supports advanced features like transactions and constraints.

### Pydantic
Pydantic is a data validation library for Python. It uses Python type hints to validate incoming data and ensures that only correctly formatted requests are processed. Pydantic automatically generates error messages when data doesn't match the expected schema, reducing manual validation code.

### Docker
Docker containerizes the application and its dependencies, including PostgreSQL. This ensures the application runs consistently across different environments—development, testing, and production. Docker eliminates the "works on my machine" problem.

## Features

- Complete CRUD operations (Create, Read, Update, Delete)
- RESTful API with FastAPI
- SQLAlchemy ORM models for database abstraction
- Pydantic schemas for request/response validation
- PostgreSQL database with Docker
- Automatic API documentation (Swagger UI)
- Type hints throughout the codebase
- Clean project structure and separation of concerns

## Project Structure

```
Python Crud Application/
├── main.py                 # Application entry point and API routes
├── models.py              # SQLAlchemy ORM models
├── schemas.py             # Pydantic validation schemas
├── database.py            # Database connection and session management
├── docker-compose.yml     # Docker configuration for PostgreSQL
├── requirements.txt       # Python dependencies
└── README.md             # Documentation
```

## Getting Started

### Prerequisites

- Docker and Docker Compose installed
- Python 3.8 or higher
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/muhammadhussain-2009/Open-Source-LLM-Projects.git
cd Open-Source-LLM-Projects/"Python Crud Application"
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start PostgreSQL using Docker:
```bash
docker-compose up -d
```

4. Run the application:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

FastAPI automatically generates interactive API documentation. Access it at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## CRUD Operations

### Create
Send a POST request to create a new resource with validated data:
```bash
POST /items/
```

### Read
Retrieve resources by ID or list all resources:
```bash
GET /items/
GET /items/{id}
```

### Update
Modify an existing resource:
```bash
PUT /items/{id}
```

### Delete
Remove a resource:
```bash
DELETE /items/{id}
```

## Database Schema

The application uses SQLAlchemy models to define the database schema. Models are automatically reflected as PostgreSQL tables with proper constraints and relationships.

## Development

### Running Tests

```bash
pytest
```

### Database Migrations

Use Alembic for database migrations (if configured):
```bash
alembic upgrade head
```

### Docker Management

Stop PostgreSQL:
```bash
docker-compose down
```

View database logs:
```bash
docker-compose logs postgres
```

## Environment Variables

Configure the following environment variables for your deployment:

```
DATABASE_URL=postgresql://user:password@localhost/dbname
DEBUG=False
SECRET_KEY=your-secret-key-here
```

## Error Handling

Pydantic provides automatic validation and error responses. Invalid requests return detailed error messages indicating which fields failed validation and why.

## Performance Considerations

- SQLAlchemy queries are optimized with proper indexing
- FastAPI handles concurrent requests efficiently
- PostgreSQL provides reliable data persistence
- Docker isolation prevents resource conflicts

## Production Deployment

For production deployment:

1. Set `DEBUG=False` in environment variables
2. Use a production ASGI server like Gunicorn:
   ```bash
   gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker
   ```
3. Use a reverse proxy like Nginx
4. Enable HTTPS with SSL certificates
5. Configure proper database backups
6. Use environment-specific configuration

## Common Issues

### Database Connection Refused
Ensure PostgreSQL container is running:
```bash
docker-compose ps
```

### Port Already in Use
Change the port in docker-compose.yml or stop conflicting services.

### Module Not Found
Install all dependencies:
```bash
pip install -r requirements.txt
```

## Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Docker Documentation](https://docs.docker.com/)

## Contributing

Contributions are welcome. Please fork the repository and submit a pull request with your improvements.

## License

This project is part of the Open-Source-LLM-Projects repository. See the main repository for licensing information.

## Contact

For questions or suggestions, please open an issue on the GitHub repository.
