# Learnify

This is a Learnify backend API, a FastAPI-based project with PostgreSQL as the database and SQLAlchemy as the ORM. This README provides comprehensive instructions on setting up, running, and contributing to the project.

## Prerequisites

- Python 3.8+
- PostgreSQL or Sqlite
- Git

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
```

### 3. Install Requirements

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Create and Configure `.env` File

Copy the `.env.example` to `.env` and update it with your environment variables:

```bash
cp .env.example .env
```

Update the `.env` file with your database credentials and other necessary environment variables:

```env
DB_HOST=localhost
DB_PORT=5432
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
DB_NAME=your_database_name
DB_TYPE=postgresql
```
If a new env is introduced, please update the env-example

### 5. Set Up the Database

Ensure your PostgreSQL server is running and the database specified in the `.env` file is created.

### 6. Run Alembic Migrations

Alembic is used for managing database migrations. To set up Alembic and run migrations:

1. Initialize Alembic (if not already initialized):

   ```bash
   alembic init migrations
   ```

2. Generate a new migration:

   ```bash
   alembic revision --autogenerate -m "Initial migration"
   ```

3. Apply the migration to the database:

   ```bash
   alembic upgrade head
   ```

### 7. Running the Application

Run the FastAPI application with Uvicorn:

```bash
python3 main.py
```

The app should now be running at `http://localhost:5000`.

## Contributing

### 1. Creating a New Branch

To contribute to this project, start by creating a new branch:

```bash
git checkout -b feat/your-feature-name
```
Pay attention to the banch naming convention

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

## Writing Clean Code

- Follow PEP 8 standards.
- Write meaningful commit messages.
- Keep functions and methods small and focused.
- Ensure your code is well-documented.
- Write tests for your code where applicable.

## Updating Dependencies

To update the dependencies, modify the `requirements.txt` file, then run:

```bash
pip install -r requirements.txt
```

Altenatively, you can update requirements.txt when u `pip install` a new package by running:

```bash
pip freeze > -r requirements.txt
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.