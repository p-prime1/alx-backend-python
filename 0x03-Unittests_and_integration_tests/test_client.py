#!/usr/bin/env python3
from utils import get_json
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """A unittest to test the GithubOrgClient module"""
    @parameterized.expand(
        [
            ("google"),
            ("abc"),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Method to test the get_json method was called once"""
        client = GithubOrgClient(org_name)

        client.org
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)

    def test_public_repos_url(self):
        """Method to unit-test the _public_repos_url"""

        test_url = "https://api.github.com/orgs/test_org"
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {'repos_url': test_url}

            obj = GithubOrgClient('test_org')
            result = obj._public_repos_url

            self.assertEqual(result, test_url)