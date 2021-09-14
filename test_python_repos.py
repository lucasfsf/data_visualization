import unittest
from python_repos import get_data_from_github

class TestGetDataFromGithub(unittest.TestCase):
    """Test the get_data_from_github function"""
    def setUp(self):
        """TODO - Setup variables to be checked by unittest"""
        self.status_code, self.total_repositories, self.repo_dicts = get_data_from_github()

    def test_status_code(self):
        """Asserts value of status code as 200"""
        self.assertEqual(self.status_code, 200)
    
    def test_total_repositories(self):
        """Asserts that the total repositories for a languare are at least 50"""
        self.assertGreater(self.total_repositories, 50)

    def test_returned_repositories_dictionaries(self):
        """Asserts that at least 20 repositories were returned"""
        self.assertGreater(len(self.repo_dicts), 19)


# Assert that the total number of repositories is greater than 20

if __name__ == "__main__":
    unittest.main()