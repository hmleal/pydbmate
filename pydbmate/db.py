import os
import re

from datetime import datetime


DATABASE_URL = ''
DEFAULT_MIGRATION_DIR = './db/migrations'
MIGRATION_TEMPLATE = '-- migrate: up\n\n\n-- migrate: down\n\n'


def ensure_dir(default_migration_dir=DEFAULT_MIGRATION_DIR):
    if os.path.exists(default_migration_dir):
        return

    os.makedirs(default_migration_dir)


def new_migration(name: str):
    """Creates a new empty migration file"""
    ensure_dir()

    filename = generate_migration_file_name(name)
    filepath = os.path.join(DEFAULT_MIGRATION_DIR, filename)

    with open(filepath, 'w+') as f:
        f.write(MIGRATION_TEMPLATE)


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

# separatorRegexp := regexp.MustCompile(`(?m)^-- migrate:(.*)$`)
