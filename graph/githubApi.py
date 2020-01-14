import requests

URL_GIT_HUB = 'https://api.github.com/'
API_BY_USER = URL_GIT_HUB + "users/%s/repos"
API_BY_REPO = URL_GIT_HUB + "repos/%s/%s"


def build_url_repos_by_user(user: str) -> str:
    return API_BY_USER % user


def build_url_detail_by_repo(user: str, repo: str) -> str:
    return API_BY_REPO % (user, repo)


def call_repos_by_user(user: str) -> dict:
    response = requests.get(
        build_url_repos_by_user(user),
    )

    l = []

    for repo in response.json():
        l.append({
            'id': repo["id"],
            'node_id': repo["node_id"],
            'name': repo["name"],
            'full_name': repo["full_name"],
            'private': repo["private"],
            'description': repo["description"],
        })

    return l


def call_detail_by_repo(user, repo) -> dict:
    response = requests.get(
        build_url_detail_by_repo(user, repo),
    )

    repo = response.json()

    d = {
        'id': repo['id'],
        'node_id': repo["node_id"],
        'name': repo['name'],
        'full_name': repo["full_name"],
        'private': repo["private"],
        'description': repo["description"]
    }

    return d
