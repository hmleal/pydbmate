import os
import unittest

from pydbmate import core
from pydbmate import settings


class TestCore(unittest.TestCase):

    def test_new_migration_file(self):
        core.new_migration('migration')

        self.assertTrue(os.path.exists(settings.PYDBMATE_BASE_DIR))
