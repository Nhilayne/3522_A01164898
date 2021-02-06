class User:
    """
    Stores data related to a user
    """
    def __init__(self, name, age, bank_info, budget_list):
        self._name = name
        self._age = age
        self._bank_info = bank_info
        self._budget_list = budget_list

    def add_transaction(self, time, amount, budget_type, merchant_name):
        self._bank_info.add_transaction(time, amount, budget_type, merchant_name)

    def display_bank_info(self):
        print("Bank Name: " + str(self._bank_info.get_name()))
        print("Account Number: " + str(self._bank_info.get_account_number()))
        print("Account Balance: $" + str(self._bank_info.get_balance()))

    def list_transactions(self):
        self._bank_info.list_transactions()

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_bank_info(self):
        return self._bank_info

    def get_budget_list(self):
        return self._budget_list

    def set_name(self, value):
        self._name = value

    def set_age(self, value):
        self._age = value

    def set_bank_info(self, value):
        self._bank_info = value

    def set_budget_list(self, value):
        self._budget_list = value
