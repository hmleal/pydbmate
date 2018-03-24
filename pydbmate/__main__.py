"""Pydbmate

Usage:
  main.py new <filename>
  main.py migrate
  main.py (-h | --help)
  main.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
from docopt import docopt

from pydbmate import db


def main(args=None):
    args = docopt(__doc__, version='Pydbmate')

    if args['new']:
        db.new_migration(args['<filename>'])

    if args['migrate']:
        pass
        # db.parse_migration_file('filename.sql')


if __name__ == '__main__':
    main()