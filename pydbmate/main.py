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
import db

from docopt import docopt


if __name__ == '__main__':
    args = docopt(__doc__, version='Pydbmate')

    if args['new']:
        db.new_migration(args['<filename>'])

    if args['migrate']:
        db.parse_migration_file('filename.sql')
        import ipdb; ipdb.set_trace()
