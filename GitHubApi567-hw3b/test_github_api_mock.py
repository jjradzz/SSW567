import unittest
from unittest import mock
from github_api import get_repos, get_commits


class MockResponse:
    """Simulates the response object returned by requests.get()"""
    def __init__(self, text, status_code=200):
        self.text = text
        self.status_code = status_code


class TestGitHubAPIMock(unittest.TestCase):

    @mock.patch('requests.get')
    def test_get_repos_returns_list(self, mock_get):
        mock_get.return_value = MockResponse('[{"name":"repo1"},{"name":"repo2"}]')
        result = get_repos("fakeuser")
        self.assertIsInstance(result, list)

    @mock.patch('requests.get')
    def test_get_repos_correct_names(self, mock_get):
        mock_get.return_value = MockResponse('[{"name":"repo1"},{"name":"repo2"}]')
        result = get_repos("fakeuser")
        self.assertIn("repo1", result)
        self.assertIn("repo2", result)

    @mock.patch('requests.get')
    def test_get_repos_invalid_user(self, mock_get):
        mock_get.return_value = MockResponse('{"message":"Not Found"}', 404)
        result = get_repos("invaliduser")
        self.assertEqual(result, "Invalid user")

    @mock.patch('requests.get')
    def test_get_repos_empty(self, mock_get):
        mock_get.return_value = MockResponse('[]')
        result = get_repos("fakeuser")
        self.assertEqual(result, [])

    @mock.patch('requests.get')
    def test_get_commits_count(self, mock_get):
        mock_get.return_value = MockResponse('[{"sha":"abc"},{"sha":"def"},{"sha":"ghi"}]')
        result = get_commits("fakeuser", "fakerepo")
        self.assertEqual(result, 3)

    @mock.patch('requests.get')
    def test_get_commits_invalid_repo(self, mock_get):
        mock_get.return_value = MockResponse('{"message":"Not Found"}', 404)
        result = get_commits("fakeuser", "invalidrepo")
        self.assertEqual(result, 0)

    @mock.patch('requests.get')
    def test_get_commits_empty(self, mock_get):
        mock_get.return_value = MockResponse('[]')
        result = get_commits("fakeuser", "fakerepo")
        self.assertEqual(result, 0)

    @mock.patch('requests.get')
    def test_get_commits_single(self, mock_get):
        mock_get.return_value = MockResponse('[{"sha":"abc"}]')
        result = get_commits("fakeuser", "fakerepo")
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()