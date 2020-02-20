#!/usr/bin/python3
"""Test"""
import unittest
import pep8


class test_City(unittest.TestCase):
    """Class test full"""
    def test_pep8_base_model(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city'])


if __name__ == '__main__':
    unittest.main()
