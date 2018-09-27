import unittest
from user import User


class TestUser(unittest.TestCase):
    """
	Test class that defines test cases for the user class behaviours.
	Args:
		unittest.TestCase: helps in creating test cases
	"""

    def setUp(self):
        """
		Function to create a user account before each test
		"""
        self.new_user = User("Kellen", "Njoroge", "boo98")
        self.new_user = User("Kellen", "Njoroge", "boo98")

    def test__init__(self):
        """
		Test to if check the initialization/creation of user instances is properly done
		"""
        self.assertEqual(self.new_user.first_name, "Kellen")
        self.assertEqual(self.new_user.last_name, "Njoroge")
        self.assertEqual(self.new_user.password, "boo98")

    def test_save_user(self):
        """
		Test to check if the new users info is saved into the users list
		"""
        self.new_user.save_user()
        self.assertEqual(len(User.users_list), 1)
