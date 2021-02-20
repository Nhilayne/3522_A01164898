from angel import Angel
from troublemaker import Troublemaker
from rebel import Rebel
from bankinfo import BankInfo
from budget import Budget


class UserList:
    """
    Stores a list of registered users
    """
    def __init__(self, user_list):
        """
        UserList constructor
        :param user_list: user list as list of users
        """
        self._user_list = user_list

    def add_user(self, new_user):
        """
        Appends a new user to the list of registered users
        :param new_user: new user as User
        :return: None
        """
        self._user_list.append(new_user)

    def get_user_by_account(self, account_num):
        """
        Returns a user with specified account_num
        :param account_num: account number as string
        :return: user, -1 if not found
        """
        for account in self._user_list:
            if account.get_bank_info().get_account_number() == account_num:
                return account
        return -1

    @staticmethod
    def create_user():
        """
        Provides a user with a console interface to create a new user.
        :return: new user as User
        """
        print("Please enter your name:")
        user_name = input(">> ")
        while True:
            print("Please enter your age:")
            user_age = input(">> ")
            if user_age.isdigit():
                user_age = int(user_age)
                break
            else:
                print("Invalid age.")
        print("Please enter your Bank's name:")
        bank_name = input(">> ")
        print("Please enter your account number:")
        account_num = input(">> ")
        while True:
            print("Please enter your account balance:")
            balance = input(">> ")
            try:
                balance = float(balance)
                break
            except ValueError:
                print("Invalid balance")
        budget_list = []
        print("How many budgets would you like to create:")
        num_budgets = input(">> ")
        for i in range(int(num_budgets)):
            print("Please enter the budget name:")
            budget_name = input(">> ")
            while True:
                print("Please enter the budget limit:")
                limit = input(">> ")
                try:
                    budget_limit = float(limit)
                    break
                except ValueError:
                    print("Invalid limit.")
            budget_list.append(Budget(budget_name, float(budget_limit)))
        bank_info = BankInfo(bank_name, account_num, balance)
        while True:
            print("Please select your user type:")
            print("1: Angel")
            print("2: Troublemaker")
            print("3: Rebel")
            user_type = input(">> ")
            if user_type == "1":
                user = Angel(user_name, user_age, bank_info, budget_list)
                break
            elif user_type == "2":
                user = Troublemaker(user_name, user_age, bank_info, budget_list)
                break
            elif user_type == "3":
                user = Rebel(user_name, user_age, bank_info, budget_list)
                break
            print("Invalid selection")
        return user

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
        test_user = Rebel("John Doe", "20", test_bank_info, test_budget_list)
        return test_user
