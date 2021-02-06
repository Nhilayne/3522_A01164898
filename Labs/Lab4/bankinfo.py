from transaction import Transaction


class BankInfo:
    """
    Stores data related to a user's bank account.
    """

    def __init__(self, name, account_number, balance):
        self._name = name
        self._account_number = account_number
        self._balance = balance
        self._transactions = []

    def add_transaction(self, time, amount, budget_type, merchant_name):
        """
        Appends a new transaction to the list of transactions
        """
        new_transaction = Transaction(time, amount, budget_type, merchant_name)
        self._transactions.append(new_transaction)

    def list_transactions(self):
        """
        Prints all transactions in order of addition to list
        """
        for transaction in self._transactions:
            count = 1
            print("-------------------------------------")
            print("Transaction " + str(count))
            print("Transaction time: " + str(transaction.get_time()))
            print("Transaction amount: " + str(transaction.get_amount()))
            print("Transaction budget: " + str(transaction.get_budget_type()))
            print("Transaction merchant: " + str(transaction.get_merchant_name()))
            count += 1

    def list_transactions_by_budget(self, budget_type):
        """
        Print all transactions of a budget type
        :param budget_type name of budget this transaction is linked to
        """
        for transaction in self._transactions:
            if budget_type == transaction.get_budget_type:
                print(transaction.get_time)
                print(transaction.get_amount)
                print(transaction.get_merchant_name)

    def get_name(self):
        return self._name

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def get_transactions(self):
        return self._transactions

    def set_name(self, value):
        self._name = value

    def set_account_number(self, value):
        self._account_number = value

    def set_balance(self, value):
        self._balance = value

    def set_transactions(self, value):
        self._transactions = value
