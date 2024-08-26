"""Seed data into db
"""
from api.v1.models.user import User
from api.db.database import create_database, get_db

create_database()
db = next(get_db())


admin_user = User(
    email="Isaacj@gmail.com",
    # password=user_service.hash_password("45@&tuTU"),
    password="test_password",
    first_name="Isaac",
    last_name="John",
    is_deleted=False,
    is_verified=True,
)
db.add(admin_user)
db.commit()

print("Seed data succesfully")