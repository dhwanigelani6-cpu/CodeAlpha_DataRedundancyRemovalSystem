import sqlite3

DATABASE = "records.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL
            )
        """)
        connection.commit()


def add_record(name, email, phone):
    with get_connection() as connection:
        connection.execute(
            "INSERT INTO records (name, email, phone) VALUES (?, ?, ?)",
            (name, email, phone)
        )
        connection.commit()


def get_records():
    with get_connection() as connection:
        return connection.execute(
            "SELECT * FROM records ORDER BY id DESC"
        ).fetchall()
