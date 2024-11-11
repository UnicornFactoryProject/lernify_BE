# Learnify

Learnify is a backend API built with FastAPI, using PostgreSQL as the database and SQLAlchemy as the ORM. This API serves as the backend for Learnify's application, handling user authentication, data management, and more.

This README provides comprehensive instructions on setting up, running, and contributing to the project.

---

## Prerequisites

Ensure the following are installed before you start:

- Python 3.8+
- PostgreSQL or SQLite
- Git

---

## Getting Started

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Requirements

Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 4. Create and Configure the `.env` File

Copy the `.env.example` file to `.env` and update it with your environment variables:

```bash
cp .env.example .env
```

Update the `.env` file with your PostgreSQL credentials and other necessary environment variables:

```bash
DB_HOST=localhost
DB_PORT=5432
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
DB_NAME=your_database_name
DB_TYPE=postgresql
```

> **Note**: If any new environment variables are added in the future, make sure to update the `.env.example` file accordingly.

### 5. Set Up the Database

Make sure your PostgreSQL server is running and the database specified in the `.env` file is created.

### 6. Run Alembic Migrations

Alembic is used for database migrations. To initialize Alembic and run the migrations:

#### Initialize Alembic (if not already done):

```bash
alembic init migrations
```

#### Generate a New Migration:

```bash
alembic revision --autogenerate -m "Initial migration"
```

#### Apply the Migration:

```bash
alembic upgrade head
```

### 7. Running the Application

You can run the FastAPI application using Uvicorn:

```bash
python3 main.py
```

The app should now be running at `http://localhost:5000`.

---

## Project Structure

This project is organized as follows:

```
project_name/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── user.py                # User-related endpoints
│   │   │   ├── auth.py                # Authentication-related endpoints
│   │   │   └── ...                    # Additional route files for version 1
│   │   ├── __init__.py
│   │   └── dependencies.py            # Common dependencies (e.g., DB session, JWT verification)
│   ├── core/
│   │   ├── config.py                  # Configuration settings
│   │   ├── security.py                # Authentication & authorization functions
│   │   └── logging.py                 # Logging setup
│   ├── models/
│   │   ├── user.py                    # Database models
│   │   └── ...
│   ├── schemas/
│   │   ├── user.py                    # Pydantic models for data validation
│   │   └── ...
│   ├── services/
│   │   ├── user_service.py            # Business logic for users
│   │   └── ...
│   ├── db/
│   │   ├── base.py                    # Base DB class & session creation
│   │   ├── init_db.py                 # DB initialization scripts
│   │   └── ...
│   ├── main.py                        # FastAPI app entry point
│   └── __init__.py
├── tests/
│   ├── v1/
│   │   ├── test_user.py
│   │   ├── test_auth.py
│   │   └── ...
│   ├── conftest.py                    # Test configurations & fixtures
│   └── __init__.py
├── .env                               # Environment variables (if any)
├── .gitignore
├── alembic.ini                        # Alembic configuration for migrations
├── README.md
└── requirements.txt
```

### Key Directories and Files

- **`app/api/v1/`**: Contains the route files (e.g., `user.py`, `auth.py`) for API version 1.
- **`app/core/`**: Configuration, security, and logging files.
- **`app/models/`**: SQLAlchemy models for database entities.
- **`app/schemas/`**: Pydantic models for validating request and response data.
- **`app/services/`**: Contains the business logic (e.g., `user_service.py`).
- **`app/db/`**: Database session and migration management.
- **`tests/`**: Contains test files for each version of the API.

---

## Contributing

### 1. Creating a New Branch

To contribute to this project, start by creating a new branch:

```bash
git checkout -b feat/your-feature-name
```

Pay attention to the branch naming convention (`feat/` for features, `fix/` for bug fixes, etc.).

### 2. Making Changes

Make your changes in the new branch. Ensure your code is clean, well-documented, and adheres to PEP 8 standards.

### 3. Testing Your Changes

Before submitting your changes, test them locally to ensure everything works as expected.

### 4. Pushing Your Changes

Push your branch to the remote repository:

```bash
git push origin feat/your-feature-name
```

### 5. Creating a Pull Request

Once your changes are pushed, create a pull request (PR) to the `dev` branch. Include a detailed description of the changes you made.

### 6. Code Review

Your PR will be reviewed by the maintainers. Please address any feedback promptly.

### 7. Merging

After approval, your PR will be merged into the `dev` branch.

---

## Writing Clean Code

- Follow **PEP 8** standards.
- Write meaningful **commit messages**.
- Keep **functions and methods small** and focused.
- Ensure your code is **well-documented**.
- Write **tests** for your code where applicable.

---

## Updating Dependencies

To update the dependencies, modify the `requirements.txt` file, then run:

```bash
pip install -r requirements.txt
```

Alternatively, you can update `requirements.txt` when you install a new package by running:

```bash
pip freeze > requirements.txt
```

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---
