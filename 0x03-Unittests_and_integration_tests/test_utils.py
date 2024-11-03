#!/usr/bin/env python3
"""Module contains a class that test the functions in utils"""
from utils import access_nested_map as access_nested
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Class uses the unittest module to test the nested_map func"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a":{"b":{"c":2}}}, ("a", "b", "c"), 2),
        ({"a":{"b":3}}, ("a", "c"), KeyError),
        ({"b":{"b":"c"}}, ("b", "b"), "c"),
        ({}, (), {}),
        ({}, ("a"), KeyError),
        ({"a":('a', 'a'),}, ("a"), ('a', 'a')),
        ({"a":1}, (), {"a":1}),
        ({"a": {"b": 2}}, ("a"), {"b":2}),
        ])

    def test_access_nested_map(self, nested_map, path, result):
        if result is KeyError:
            with self.assertRaises(KeyError):
                access_nested(nested_map, path)
        else:
            self.assertEqual(access_nested(nested_map, path), result)

if __name__ == "__main__":
    unittest.main()
