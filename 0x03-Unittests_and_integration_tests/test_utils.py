#!/usr/bin/env python3
"""
Test module for access_nested_map from utils.
Includes unit tests with parameterized inputs.
"""


from utils import access_nested_map, get_json
import unittest
from parameterized import parameterized
from unittest.mock import patch


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


class TestGetJson(unittest.TestCase):
    """
    Unit Test for testing the get_json function in the
    utils model
    """

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("utils.requests.get")
    def test_get_json(self, url, payload, mock_get):
        """
        Test that the get_json returns the expected result
        """
        mock_get.return_value.json.return_value = payload

        result = get_json(url)
        self.assertEqual(result, payload)
        mock_get.assert_called_once_with(url)
