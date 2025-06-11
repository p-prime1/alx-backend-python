#!/usr/bin/env python3
"""Test module for the client module"""


from utils import get_json
import unittest
from parameterized import parameterized, parameterized_class
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
        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {"repos_url": test_url}

            obj = GithubOrgClient("test_org")
            result = obj._public_repos_url

            self.assertEqual(result, test_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Method to unit-test the _public_repos_url accepts a
        mock_get_json arg"""
        mock_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "mit"}},
        ]
        mock_get_json.return_value = mock_payload

        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_ur:
            mock_ur.return_value = "https://api.github.com/orgs/test_org/repos"

            obj = GithubOrgClient("test_org")
            result = obj.public_repos()
            expected_repos = ["repo1", "repo2", "repo3"]

            self.assertEqual(result, expected_repos)
            mock_ur.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test_org/repos"
            )
    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, license_key="my_license", True)
            ({"license": {"key": "other_license"}}, license_key="my_license", True)
        ]
    )
    def test_has_license(self, repo, license, result):
        """Mehtod to tet the has_license method"""
        has_license = GithubOrgClient.has_license()
        self.assertEqual(has_license(repo, license), result)

@parameterized_class(
    [
        ('org_payload'),
        ('repos_payload'),
        ('expected_repos'),
        ('apache2_repos'),
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Class integrates test the GithubClient class"""
    def setupClass(self, payload):
        self.get_patcher = patch("utils.request.get")
        self.mock_get_patcher = self.get_patcher.start()
        self.mock_get_patcher.side_effect = payload

    def tearDownClass(self):
        self.mock_get_patcher.stop()

