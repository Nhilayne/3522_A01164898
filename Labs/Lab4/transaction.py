class Transaction:
    """
    Store the properties of a transaction
    """
    def __init__(self, time, amount, budget_type, merchant_name):
        self._time = time
        self._amount = amount
        self._budget_type = budget_type
        self._merchant_name = merchant_name

    def get_time(self):
        return self._time

    def set_time(self, value):
        self._time = value

    def get_amount(self):
        return self._amount

    def set_amount(self, value):
        self._amount = value

    def get_budget_type(self):
        return self._budget_type

    def set_budget_type(self, value):
        self._budget_type = value

    def get_merchant_name(self):
        return self._merchant_name

    def set_set_merchant_name(self, value):
        self._merchant_name = value
