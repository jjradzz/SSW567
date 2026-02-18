import requests
import json


def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    resp = requests.get(url)
    if resp.status_code != 200:
        return "Invalid user"
    repos = json.loads(resp.text)
    return [repo["name"] for repo in repos]


def get_commits(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
    resp = requests.get(url)
    if resp.status_code != 200:
        return 0
    commits = json.loads(resp.text)
    return len(commits)


def get_user_repos_and_commits(username):
    repos = get_repos(username)
    if repos == "Invalid user":
        print("Invalid user")
        return
    for repo in repos:
        num_commits = get_commits(username, repo)
        print(f"Repo: {repo} Number of commits: {num_commits}")
