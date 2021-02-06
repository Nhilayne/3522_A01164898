from userlist import UserList


class Menu:
    """
    Allows a user to interact with the program
    """

    def __init__(self):
        """
        Menu constructor
        """
        self._user_list = []
        self._current_user = None

    def menu_start(self):
        """
        This is the main user interface of the program
        :return: None
        """
        print("---------------------Welcome to the F.A.M---------------------")
        while True:
            print("\n================================================\n")
            print("Please select an action by entering the corresponding number:")
            print("1: Create New User (Non-functional)")
            print("2: Login As Existing User (Non-functional)")
            print("3: Create and Login As Test User")
            print("0: Exit")
            user_input = input(">> ")
            if user_input == "0":
                print("Exiting program")
                break
            elif user_input == "2":
                # print("Please enter your account number:")
                # user_input = input(">> ")
                continue
            elif user_input == "3":
                print("Creating Test User")
                test_user = UserList.load_test_user()
                self._user_list = UserList(test_user)
                self._current_user = test_user
                while True:
                    print("\n================================================\n")
                    print("Welcome " + str(self._current_user.get_name()))
                    print("What would you like to do today?")
                    print("1: View Budgets (Non-functional)")
                    print("2: Record A New Transaction")
                    print("3: View Transactions By Budget (Non-functional)")
                    print("4: View Account Summary")
                    print("0: Exit")
                    logged_in_input = input(">> ")
                    if logged_in_input == "0":
                        print("Exiting your account menu.")
                        break
                    elif logged_in_input == "1":
                        continue
                    elif logged_in_input == "2":
                        print("Please enter the time of the transaction: ")
                        transaction_time = input(">>")
                        print("Please enter the amount of the transaction: ")
                        transaction_amount = input(">>")
                        print("Please enter the budget to apply for this transaction: ")
                        transaction_budget = input(">>")
                        print("Please enter the name of the seller for this transaction: ")
                        transaction_merchant = input(">>")
                        self._current_user.add_transaction(transaction_time, transaction_amount,
                                                           transaction_budget, transaction_merchant)
                    elif logged_in_input == "3":
                        continue
                    elif logged_in_input == "4":
                        print("\n================================================\n")
                        print("Your Account Information is:")
                        self._current_user.display_bank_info()
                        self._current_user.list_transactions()
                    else:
                        continue
            else:
                print("Invalid input")
                continue


def main():
    """
    Main function of the program, creates and calls the user interface
    :return: None
    """
    fam_menu = Menu()
    fam_menu.menu_start()


if __name__ == '__main__':
    main()
