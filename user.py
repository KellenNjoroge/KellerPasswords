class User:
    """
	Basic user info

	"""

    users_list = []

    def __init__(self, first_name, last_name, password):
        """
		Each and every user will have the following variables
		"""

        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        """
		Function to save a newly created user instance
		"""
        User.users_list.append(self)
