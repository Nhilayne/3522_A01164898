from transaction import Transaction


class BankInfo:
    """
    Stores data related to a user's bank account.
    """
    def __init__(self, name, account_number, balance):
        """
        Initialize bank info object
        :param name: bank name as string
        :param account_number: bank account number as string
        :param balance: bank account balance as float
        """
        self._name = name
        self._account_number = account_number
        self._balance = balance
        self._transactions = []

    def add_transaction(self, time, amount, budget_type, merchant_name):
        """
        Appends a new transaction to the list of transactions
        :param time: time as datetime
        :param amount: amount as float
        :param budget_type: budget name as string
        :param merchant_name: merchant name as string
        :return: None
        """
        new_transaction = Transaction(time, amount, budget_type, merchant_name)
        self._transactions.append(new_transaction)

    def list_transactions(self):
        """
        Prints all transactions in order of addition to list
        :return: None
        """
        count = 1
        for transaction in self._transactions:
            print("-------------------------------------")
            print("Transaction " + str(count))
            print("Transaction time: " + str(transaction.get_time()))
            print("Transaction amount: " + str(transaction.get_amount()))
            print("Transaction budget: " + str(transaction.get_budget_type()))
            print("Transaction merchant: " + str(transaction.get_merchant_name()))
            count += 1

    def list_transactions_by_budget(self, budget_type):
        """
        Lists all transactions of a specified budget
        :param budget_type: Budget name as string
        :return: None
        """
        count = 1
        for transaction in self._transactions:
            if budget_type == transaction.get_budget_type():
                print("-------------------------------------")
                print("Transaction " + str(count))
                print("Transaction time: " + str(transaction.get_time()))
                print("Transaction amount: " + str(transaction.get_amount()))
                print("Transaction budget: " + str(transaction.get_budget_type()))
                print("Transaction merchant: " + str(transaction.get_merchant_name()))
                count += 1

    def get_name(self):
        """
        Get Bank Name
        :return: name as string
        """
        return self._name

    def get_account_number(self):
        """
        Get Bank Account number
        :return: account number as string
        """
        return self._account_number

    def get_balance(self):
        """
        Get account balance
        :return: balance as float
        """
        return self._balance

    def get_transactions(self):
        """
        Get transactions
        :return: transactions as list
        """
        return self._transactions

    def set_name(self, value):
        """
        Set Bank Name
        :param value: name as string
        :return: None
        """
        self._name = value

    def set_account_number(self, value):
        """
        Set account number
        :param value: account number as string
        :return: None
        """
        self._account_number = value

    def set_balance(self, value):
        """
        Set Account balance
        :param value: balance as float
        :return: None
        """
        self._balance = value

    def set_transactions(self, value):
        """
        Set transaction list
        :param value: transactions as list of transactions
        :return: None
        """
        self._transactions = value
