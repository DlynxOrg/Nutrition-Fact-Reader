# FastAPI Project Folder Structure

This document outlines the recommended folder structure for a FastAPI project using Hatchet as a worker manager. The structure is designed for scalability, maintainability, and clarity.

## Folder Structure

```
fastapi_project/
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
├── uv.lock
├── img.webp
├── src/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # Entry point for the FastAPI app
│   │   ├── config.py        # Configuration settings
│   │   ├── database/        # Database connection logic
│   │   ├── dependencies.py  # Dependency injection
│   │   ├── routers/         # API route definitions
│   │   ├── repositories/    # Database interaction layer
│   │   │   ├── __init__.py
│   │   │   ├── example.py   # Example route
│   │   ├── models/          # Database models
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   ├── schemas/         # Pydantic models for request/response validation
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   ├── services/        # Business logic
│   │   │   ├── __init__.py
│   │   │   ├── example_service.py  # Example service
│   │   ├── tasks/           # Task definitions managed by Hatchet
│   │   │   ├── __init__.py
│   │   │   ├── example_task.py
│   │   ├── workers/         # Worker implementations managed by Hatchet
│   │   │   ├── __init__.py
│   │   │   ├── hatchet_worker.py  # Hatchet worker integration
│   ├── tests/               # Unit and integration tests
│   │   ├── __init__.py
│   │   ├── test_main.py
```

## Explanation of Key Folders and Files

1. **`src/app/main.py`**: The entry point for the FastAPI application. It initializes the app and includes the routers.
2. **`src/app/config.py`**: Contains configuration settings, such as environment variables.
3. **`src/app/dependencies.py`**: Defines reusable dependencies for dependency injection.
4. **`src/app/routers/`**: Contains all API route definitions, organized by feature.
5. **`src/app/models/`**: Defines database models using an ORM like SQLAlchemy.
6. **`src/app/schemas/`**: Contains Pydantic models for request and response validation.
7. **`src/app/services/`**: Contains business logic that is independent of tasks and workers.
8. **`src/app/tasks/`**: Defines tasks managed by Hatchet SDK.
9. **`src/app/workers/`**: Implements workers managed by Hatchet SDK, including integrations like `hatchet_worker.py`.
8. **`src/app/utils/`**: Contains utility functions and helpers.
9. **`src/tests/`**: Includes unit and integration tests for the application.

## Next Steps

Populate the placeholder files with the necessary code for your application. Follow the structure to ensure a clean and maintainable codebase.