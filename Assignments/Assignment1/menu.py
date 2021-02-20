from userlist import UserList
from datetime import date


class Menu:
    """
    Provides a console interface for a user to interact with
    """

    def __init__(self):
        """
        Menu constructor
        """
        self._user_list = UserList([])
        self._current_user = None

    def menu_start(self):
        """
        This is the main user interface of the program
        :return: None
        """
        print("\n---------------------Welcome to the F.A.M---------------------")
        while True:
            print("\n================================================\n")
            print("Please select an action by entering the corresponding number:")
            print("1: Create New User")
            print("2: Login As Existing User")
            print("3: Create Test User and Login")
            print("0: Exit")
            user_input = input(">> ")
            if user_input == "0":
                print("Exiting program")
                break
            elif user_input == "1":
                new_user = self._user_list.create_user()
                self._user_list.add_user(new_user)
                print("Login as newly created user?")
                print("1: Yes")
                print("0: No")
                user_input = input(">> ")
                if user_input == "1":
                    self._current_user = new_user
                    self.login()
                continue
            elif user_input == "2":
                print("Please enter your account number:")
                user_input = input(">> ")
                loaded_account = self._user_list.get_user_by_account(user_input)
                if loaded_account != -1:
                    self._current_user = loaded_account
                    self.login()
                elif loaded_account == -1:
                    print("Account Number not found")
                continue
            elif user_input == "3":
                print("Creating Test User and logging in")
                test_user = UserList.load_test_user()
                self._user_list.add_user(test_user)
                self._current_user = test_user
                self.login()
            else:
                print("Invalid input")
                continue

    def login(self):
        """
        Provides a console interface for a user once they have logged in
        :return: None
        """
        while True:
            print("\n================================================\n")
            print("Welcome " + str(self._current_user.get_name()))
            print("What would you like to do today?")
            print("1: View Budgets")
            print("2: Record A New Transaction")
            print("3: View Transactions By Budget")
            print("4: View Account Summary")
            print("0: Exit")
            logged_in_input = input(">> ")
            if logged_in_input == "0":
                print("Exiting your account menu.")
                break
            elif logged_in_input == "1":
                # view budgets
                print("Budget Summary:")
                for budget in self._current_user.get_budget_list():
                    print("-------------------------------------")
                    print("Budget Type: "+str(budget.get_budget_type()))
                    print("Budget Locked: " + str(budget.get_locked()))
                    print("Budget Spent: " + str(budget.get_budget_spent()))
                    print("Budget Remaining: " + str(budget.get_budget_remaining()))
                    print("Budget total: " + str(budget.get_budget_target()))
                continue
            elif logged_in_input == "2":
                # create transaction
                # self._current_user.get_bank_info.create_transaction()
                transaction_time = date.today().strftime("%B/%d/%Y")
                # print("Please enter the amount of the transaction: ")
                # transaction_amount = input(">>")
                while True:
                    print("Please enter the amount of the transaction: ")
                    transaction_amount = input(">>")
                    try:
                        transaction_amount = float(transaction_amount)
                        break
                    except ValueError:
                        print("Invalid amount.")
                print("Please select a budget to apply for this transaction: ")
                budgets = self._current_user.get_budget_list()
                counter = 1
                for budget in budgets:
                    print(str(counter) + ": " + str(budget.get_budget_type()))
                    counter += 1
                while True:
                    selection = input(">>")
                    if int(selection) - 1 <= len(budgets):
                        budget_list = self._current_user.get_budget_list()
                        transaction_budget = budget_list[int(selection)-1].get_budget_type()
                        break
                    else:
                        print("Invalid selection.")

                print("Please enter the name of the seller for this transaction: ")
                transaction_merchant = input(">>")
                self._current_user.add_transaction(transaction_time, transaction_amount,
                                                   transaction_budget, transaction_merchant)
            elif logged_in_input == "3":
                # view transactions by budget
                print("Select a Budget to see related transactions:")
                budgets = self._current_user.get_budget_list()
                print("0: Cancel")
                counter = 1
                for budget in budgets:
                    print(str(counter)+": "+str(budget.get_budget_type()))
                    counter += 1
                while True:
                    selection = input(">>")
                    if int(selection) - 1 <= len(budgets):
                        self._current_user.get_bank_info().list_transactions_by_budget(budgets[int(selection) - 1]
                                                                                       .get_budget_type())
                        break
                    else:
                        print("Invalid selection.")
            elif logged_in_input == "4":
                print("\n================================================\n")
                print("Your Account Information is:")
                self._current_user.display_bank_info()
                self._current_user.get_bank_info().list_transactions()
            else:
                continue
