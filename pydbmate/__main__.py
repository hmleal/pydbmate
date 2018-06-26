"""Pydbmate

Usage:
  pydbmate new <filename>
  pydbmate migrate
  pydbmate status
  pydbmate (-h | --help)
  pydbmate --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
from docopt import docopt

from pydbmate import core


def main(args=None):
    args = docopt(__doc__, version="Pydbmate")

    if args["new"]:
        core.new_migration(args["<filename>"])

    if args["migrate"]:
        migrations = core.parse_migration_file()
        for m in migrations:
            print(m)

    if args["migrate"]:
        raise NotImplementedError


if __name__ == "__main__":
    main()
