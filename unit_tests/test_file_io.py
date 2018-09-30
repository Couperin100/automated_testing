from os import path
import unittest

from helpers.file_io import read_yaml_file
from helpers.paths import UNIT_TESTS


class TestFileIO(unittest.TestCase):

    def setUp(self):
        """Unittest setup."""
        self.yaml_file = read_yaml_file(path.join(UNIT_TESTS, "test_yaml_file.yaml"))

    def test_read_yaml_file(self):
        """Reading a yaml file returns a dict of the correct data."""
        self.assertEqual(self.yaml_file, {
            "one_item": "one_item",
            "list_item": [
                "list one",
                "list two",
                "list three"
            ],
            "dictionary": {
                "item_one": 1,
                "item_two": 2,
                "item_three": 3
            }
        })

    def test_get_the_expected_text(self):
        """Reading a yaml file node returns the correct text."""
        self.assertEqual(self.yaml_file['one_item'], "one_item")
        self.assertEqual(self.yaml_file['list_item'], ["list one", "list two", "list three"])
        self.assertEqual(self.yaml_file['dictionary']['item_one'], 1)
