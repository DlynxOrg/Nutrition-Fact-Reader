# Project Setup

## Environment Variables

To connect to the PostgreSQL database, set the following environment variable in your `.env` file or system environment:

- `OCR_PSQL_DB_URL`: The connection string for your PostgreSQL database. It should follow the format:

  ```
  postgresql://<username>:<password>@<host>:<port>/<database_name>
  ```

  Example:

  ```
  DATABASE_URL=postgresql://user:password@localhost:5432/mydatabase
  ```

## Environment Variables

To use the OpenAI API, set the following environment variable in your `.env` file or system environment:

- `OPENAI_API_KEY`: Your OpenAI API key.

Example:
```bash
OPENAI_API_KEY=your_api_key_here
```

Ensure the API key is valid and accessible before running the application.
## Installing SDKs

To install the required SDKs, use the `uv` command to install the dependencies listed in the `pyproject.toml` file:

```bash
uv install
```

This will ensure all necessary packages are installed.

## Running the Application

To run the application, follow these steps:

1. Navigate to the application directory:
   ```bash
   cd src/app
   ```

2. Run the FastAPI app layer:
   ```bash
   uv run main.py
   ```

3. Run the Hatchet worker layer:
   ```bash
   uv run hatchet_workers.py
   ```
## API Documentation

You can access the Swagger API documentation at:

```
http://localhost:8000/docs
```
Ensure that the database is accessible and the credentials are correct before running the application.