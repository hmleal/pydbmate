import os


PYDBMATE_DB_URI = os.environ.get("PYDBMATE_DB_URI")

PYDBMATE_BASE_DIR = os.environ.get("PYDBMATE_BASE_DIR", "./db/migrations")

MIGRATION_TEMPLATE = "-- migrate: up\n\n\n-- migrate: down\n\n"

DATABASE_URL = "sqlite:///db.sqlite3"
