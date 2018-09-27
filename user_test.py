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


class TestCredentials(unittest.TestCase):
    """
	Test class that defines test cases for the credentials class behaviours.
	Args:
		unittest.TestCase: helps in creating test cases
	"""
    def setUp(self):
        """
		Function to create an account's credentials before each test
		"""
        self.new_credential = Credential('Kellen', 'Facebook', 'Kellen Njoroge', 'boo90')

    def test__init__(self):
        '''
		Test to if check the initialization/creation of credential instances is properly done
		'''
        self.assertEqual(self.new_credential.user_name, 'Kellen')
        self.assertEqual(self.new_credential.site_name, 'Facebook')
        self.assertEqual(self.new_credential.account_name, 'Kellen Njoroge')
        self.assertEqual(self.new_credential.password, 'boo90')
    @property
    def test_check_user(self):
        """
		Function to test whether the login in function check_user works as expected
		"""
        self.new_user = User("Mercy", "Kubania",  "kubz97")
        self.new_user.save_user()
        user2 = User("Mercy", "Kubania", "kubz97")
        user2.save_user()

        for user in User.users_list:
            if user.first_name == user2.first_name and user.password == user2.password:
                current_user = user.first_name
        return current_user

        self.assertEqual(current_user, Credential.check_user(user2.password, user2.first_name))


if __name__ == '__main__':
    unittest.main(verbosity=2)
