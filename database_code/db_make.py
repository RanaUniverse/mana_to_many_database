"""
Here will the code to make the table and
it will use the connection
and i will call the fun of generate the table
if the table not exists in the database
in the main.py i will import this and call to executes
"""

from sqlmodel import (
    create_engine,
    SQLModel,
)

# sqlite_file_name = "zzz_database.db"
# DATABASE_URL = f"sqlite:///{sqlite_file_name}"


DB_USERNAME = "rana"
DB_PASSWORD = "abc"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "hero2"

DATABASE_URL = (
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}" f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


engine = create_engine(url=DATABASE_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine)
