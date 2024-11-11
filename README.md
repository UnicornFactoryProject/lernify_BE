# Learnify Backend API

Learnify is a backend API for a learning platform, built using **FastAPI**, with **PostgreSQL** as the database and **SQLAlchemy** as the ORM. This README provides comprehensive instructions on setting up, running, and contributing to the project.

---

## Prerequisites

Before getting started, make sure you have the following installed:

- Python 3.8+
- PostgreSQL (or SQLite for development)
- Git

---

## Getting Started

Follow these steps to set up the project locally:

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
```

Activate the environment:
- On Windows:

  ```bash
  venv\Scripts\activate
  ```

- On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

### 3. Install Requirements

Install the project dependencies by running:

```bash
pip install -r requirements.txt
```

### 4. Create and Configure `.env` File

Copy the `.env.example` file to `.env`:

```bash
cp .env.example .env
```

Open the `.env` file and update the following environment variables with your database credentials and other necessary configurations:

```bash
DB_HOST=localhost
DB_PORT=5432
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
DB_NAME=your_database_name
DB_TYPE=postgresql
```

If a new environment variable is introduced, make sure to update `.env.example` as well.

### 5. Set Up the Database

Ensure that your PostgreSQL server is running and the database specified in the `.env` file is created.

### 6. Run Alembic Migrations

Alembic is used for managing database migrations. To set up Alembic and run migrations:

- Initialize Alembic (if it’s not already initialized):

  ```bash
  alembic init migrations
  ```

- Generate a new migration:

  ```bash
  alembic revision --autogenerate -m "Initial migration"
  ```

- Apply the migration to the database:

  ```bash
  alembic upgrade head
  ```

### 7. Running the Application

To run the FastAPI application using **Uvicorn**, execute the following command:

```bash
python3 main.py
```

The app should now be running at [http://localhost:5000](http://localhost:5000).

---

## Contributing

To contribute to the project, follow these steps:

### 1. Create a New Branch

Create a new branch for your feature or bug fix:

```bash
git checkout -b feat/your-feature-name
```

Make sure to follow the branch naming convention (e.g., `feat/`, `bugfix/`).

### 2. Make Changes

Work on your changes in the new branch. Ensure that your code adheres to PEP 8 standards, is clean, and well-documented.

### 3. Test Your Changes

Before submitting your changes, test them locally to ensure everything works as expected.

### 4. Push Your Changes

Once you’ve made your changes, push the branch to the remote repository:

```bash
git push origin feat/your-feature-name
```

### 5. Create a Pull Request

After pushing your branch, create a pull request (PR) to the `dev` branch. Provide a detailed description of the changes you made.

### 6. Code Review

Your PR will be reviewed by the maintainers. Address any feedback or suggestions promptly.

### 7. Merging

Once your PR is approved, it will be merged into the `dev` branch.

---

## Writing Clean Code

To maintain high code quality, adhere to the following guidelines:

- Follow [PEP 8](https://peps.python.org/pep-0008/) standards.
- Write clear, concise commit messages.
- Keep functions and methods small and focused on a single task.
- Ensure your code is well-documented, especially for complex logic.
- Write tests for your code where applicable.

---

## Updating Dependencies

To update project dependencies, modify the `requirements.txt` file and then run:

```bash
pip install -r requirements.txt
```

Alternatively, you can update `requirements.txt` after installing a new package:

```bash
pip freeze > requirements.txt
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

### Notes

- If you’re using SQLite instead of PostgreSQL for development, make sure to adjust the `DB_TYPE` and other database-related configurations in the `.env` file.
- For more detailed guidance on FastAPI and PostgreSQL setup, refer to their official documentation.

---
