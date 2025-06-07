#!/usr/bin/env python3
"""
Test module for access_nested_map from utils.
Includes unit tests with parameterized inputs.
"""


from utils import access_nested_map
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit test class for testing the access_nested_map function
    from the utils module.
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, result):
        """
        Test that access_nested_map returns the expected result
        for various nested structures and paths.
        """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, result):
        """
        Test that the access_nested_map raises the expected exceptions"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
