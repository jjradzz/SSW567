import unittest
from github_api import get_repos, get_commits, get_user_repos_and_commits


class TestGitHubAPI(unittest.TestCase):

    def test_get_repos_returns_list(self):
        result = get_repos("richkempinski")
        self.assertIsInstance(result, list)

    def test_get_repos_contains_known_repo(self):
        result = get_repos("richkempinski")
        self.assertIn("hellogitworld", result)

    def test_get_repos_invalid_user(self):
        result = get_repos("fakeUser_doesNOTexist12345")
        self.assertEqual(result, "Invalid user")

    def test_get_commits_returns_int(self):
        result = get_commits("richkempinski", "hellogitworld")
        self.assertIsInstance(result, int)

    def test_get_commits_greater_than_zero(self):
        result = get_commits("richkempinski", "hellogitworld")
        self.assertGreater(result, 0)

    def test_get_commits_invalid_repo(self):
        result = get_commits("richkempinski", "fakeRepo")
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()