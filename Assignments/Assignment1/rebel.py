from user import User


class Rebel(User):
    """
    Stores data related to a rebel usertype
    """

    def __init__(self, name, age, bank_info, budget_list):
        """
        Initialize Rebel object
        :param name: user name as string
        :param age: user age as int
        :param bank_info: bank info as bankinfo
        :param budget_list: budget list as list of budgets
        """
        self._name = name
        self._age = age
        self._bank_info = bank_info
        self._budget_list = budget_list

    def add_transaction(self, time, amount, budget_type, merchant_name):
        """
        Creates a new user transaction if bank balance allows, does not create transaction if balance is too low
        or if budget for transaction is locked
        :param time: time of transaction as datetime
        :param amount: amount as float
        :param budget_type: budget name as string
        :param merchant_name: merchant name as string
        :return: None
        """
        working_budget = None
        # load budget by type
        for budget in self._budget_list:
            if budget_type.lower() == budget.get_budget_type().lower():
                working_budget = budget
        if working_budget is not None:
            # check budget lockout
            if working_budget.get_locked() is False:
                # check bank balance is greater than amount spent
                if float(self._bank_info.get_balance()) >= amount:
                    self._bank_info.set_balance(float(self._bank_info.get_balance()) - amount)
                    # if everything is still good: then
                    self._bank_info.add_transaction(time, amount, working_budget.get_budget_type(), merchant_name)
                    working_budget.set_budget_spent(working_budget.get_budget_spent()+amount)
                    working_budget.update_budget_remaining()
                    # get warnings
                    print_history_warnings = self.warnings(working_budget)
                    # get notifications
                    print_history_notifications = self.notifications(working_budget)
                    # apply lockouts
                    self.lockouts(working_budget)
                    if print_history_notifications is True or print_history_warnings is True:
                        print("Transaction history for this budget:")
                        self._bank_info.list_transactions_by_budget(working_budget.get_budget_type())
                else:
                    print("Insufficient Funds")
            else:
                print("Specified Budget is Locked")
        else:
            print("Specified Budget not found")

    def display_bank_info(self):
        """
        Displays User Bank info
        :return: None
        """
        print("Bank Name: " + str(self._bank_info.get_name()))
        print("Account Number: " + str(self._bank_info.get_account_number()))
        print("Account Balance: $" + str(self._bank_info.get_balance()))

    def notifications(self, current_budget):
        """
        Checks an attempted transaction for notification flags
        :param current_budget: budget as Budget
        :return: flag thrown as boolean
        """
        # if exceeded budget in one category, be mean!! >:(
        if current_budget.get_budget_remaining() < 0:
            print("YOU HAVE EXCEEDED YOUR BUDGET; FURTHER TRANSACTIONS MAY LOCK THIS BUDGET, OR YOUR ACCOUNT.")
            return True
        return False

    def warnings(self, current_budget):
        """
        Checks an attempted transaction for warning flags
        :param current_budget: budget as Budget
        :return: flag thrown as boolean
        """
        # warn they're over 50% of their budget each time
        if (float(current_budget.get_budget_spent()) / float(current_budget.get_budget_target())) > 0.5:
            print("WARNING: You have exceeded 50% of this budget")
            return True
        return False

    def lockouts(self, current_budget):
        """
        Checks an attempted transaction for lockout flags, then locks the budget and/or account if thrown
        :param current_budget: budget as Budget
        :return: None
        """
        # lockout if exceed 100% of allotted amount
        # total lockout if 2 budgets lockout
        num_locked = 0
        #print(float(current_budget.get_budget_spent()) / float(current_budget.get_budget_target()) > 2)
        if (float(current_budget.get_budget_spent()) / float(current_budget.get_budget_target())) > 2:
            print("BUDGET LOCKED: You have exceeded this budget by too much, and will not be able to use it further")
            current_budget.set_locked(True)
        for budgets in self._budget_list:
            if budgets.get_locked() is True:
                num_locked += 1
        if num_locked > 1:
            print("ACCOUNT LOCKED: You have exceeded more than one budget by too much, "
                  "and will not be able to use your account further")
            for budgets in self._budget_list:
                budgets.set_locked(True)

    def get_name(self):
        """
        Get user name
        :return: name as string
        """
        return self._name

    def get_age(self):
        """
        Get user age
        :return: age as int
        """
        return self._age

    def get_bank_info(self):
        """
        Get user bank info
        :return: bank info as BankInfo
        """
        return self._bank_info

    def get_budget_list(self):
        """
        Get budget list
        :return: budget list as list of budgets
        """
        return self._budget_list

    def set_name(self, value):
        """
        Set user name
        :param value:name as string
        :return: None
        """
        self._name = value

    def set_age(self, value):
        """
        Set user age
        :param value: age as int
        :return: None
        """
        self._age = value

    def set_bank_info(self, value):
        """
        Set user Bank info
        :param value: bank info as BankInfo
        :return: None
        """
        self._bank_info = value

    def set_budget_list(self, value):
        """
        Set budget list
        :param value: budget list as list of budgets
        :return: None
        """
        self._budget_list = value
