import os
import re

from datetime import datetime

from pydbmate import settings


def ensure_dir():
    os.makedirs(settings.PYDBMATE_BASE_DIR, exist_ok=True)


def new_migration(name: str):
    """Creates a new empty migration file"""
    ensure_dir()

    filename = generate_migration_file_name(name)
    filepath = os.path.join(settings.PYDBMATE_BASE_DIR, filename)

    with open(filepath, 'w+') as f:
        f.write(settings.MIGRATION_TEMPLATE)


def generate_migration_file_name(suffix: str):
    pattern = '{:%Y%m%d_%H%M}_{}.sql'

    return pattern.format(datetime.now(), suffix)


def parse_migration_file(filename: str):
    filepath = os.path.join(DEFAULT_MIGRATION_DIR, filename)

    with open(filepath, 'r') as f:
        data = f.read()

    migrations = []
    for migration in re.split('^-- migrate: (?:up|down)\n', data, flags=re.MULTILINE):
        if migration:
            migrations.append(migration.strip())

    return migrations
