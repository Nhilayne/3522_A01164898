from user import User
from bankinfo import BankInfo
from budget import Budget


class UserList:
    """
    Stores a list of registered users
    """
    def __init__(self, user_list):
        """
        UserList constructor
        :param user_list: list of users
        """
        self._user_list = user_list

    def add_user(self, new_user):
        """
        Appends a new user to the list of registered users
        :param new_user: new user to append
        :return: none
        """
        self._user_list.append(new_user)

    @staticmethod
    def load_test_user():
        """
        Creates a test user with pre-set values to test the program's methods with
        :return: test user with assigned values
        """
        test_bank_info = BankInfo("RBC", "12345678", "5000.00")
        budget1 = Budget("Games and Entertainment", 1000.00)
        budget2 = Budget("Clothing and Accessories", 1000.00)
        budget3 = Budget("Eating Out", 1000.00)
        budget4 = Budget("Misc.", 1000.00)
        test_budget_list = [budget1, budget2, budget3, budget4]
        test_user = User("John Doe", "20", test_bank_info, test_budget_list)
        return test_user
