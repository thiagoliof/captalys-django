import unittest

from graph.githubApi import call_repos_by_user, build_url_repos_by_user, build_url_detail_by_repo, call_detail_by_repo


class TestRestAPI(unittest.TestCase):

    def test_build_url_by_user(self):
        self.assertEqual(build_url_repos_by_user("thiago"), "https://api.github.com/users/thiago/repos")

    def test_build_url_detail_by_repo(self):
        self.assertEqual(build_url_detail_by_repo("thiagoliof", "backend"), "https://api.github.com/repos/thiagoliof"
                                                                            "/backend")

    def test_value_in_dict_repos(self):
        response_str = call_repos_by_user("henriquebastos")
        self.assertIn('description', str(response_str))

    def test_value_in_dict_repo(self):
        response_str = call_detail_by_repo("thiagoliof", "backend")
        self.assertIn('full_name', str(response_str))

