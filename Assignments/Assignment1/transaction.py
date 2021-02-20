class Transaction:
    """
    Store the properties of a transaction
    """
    def __init__(self, time, amount, budget_type, merchant_name):
        """
        Initialize transaction
        :param time: time as datetime
        :param amount: amount as float
        :param budget_type: budget name as string
        :param merchant_name: merchant name as string
        """
        self._time = time
        self._amount = amount
        self._budget_type = budget_type
        self._merchant_name = merchant_name

    def get_time(self):
        """
        Get time of transaction
        :return: time as  datetime
        """
        return self._time

    def set_time(self, value):
        """
        Set time of transaction
        :param value: time as datetime
        :return: None
        """
        self._time = value

    def get_amount(self):
        """
        Get transaction amount
        :return: amount as float
        """
        return self._amount

    def set_amount(self, value):
        """
        Set transaction amount
        :param value: amount as float
        :return: None
        """
        self._amount = value

    def get_budget_type(self):
        """
        Get Budget name
        :return: budget as string
        """
        return self._budget_type

    def set_budget_type(self, value):
        """
        Set budget name
        :param value: budget name as string
        :return: None
        """
        self._budget_type = value

    def get_merchant_name(self):
        """
        Get merchant name
        :return: merchant name as string
        """
        return self._merchant_name

    def set_merchant_name(self, value):
        """
        Set merchant name
        :param value: merchant name as string
        :return: None
        """
        self._merchant_name = value
