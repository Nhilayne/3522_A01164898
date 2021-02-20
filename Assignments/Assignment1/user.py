from abc import ABC, abstractmethod


class User(ABC):

    @abstractmethod
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

    @abstractmethod
    def display_bank_info(self):
        """
        Displays User Bank info
        :return: None
        """

    @abstractmethod
    def notifications(self, current_budget):
        """
        Checks an attempted transaction for notification flags
        :param current_budget: budget as Budget
        :return: flag thrown as boolean
        """

    @abstractmethod
    def warnings(self, current_budget):
        """
        Checks an attempted transaction for warning flags
        :param current_budget: budget as Budget
        :return: flag thrown as boolean
        """

    @abstractmethod
    def lockouts(self, current_budget):
        """
        Checks an attempted transaction for lockout flags, then locks the budget and/or account if thrown.
        :param current_budget: budget as Budget
        :return: None
        """
        pass

    @abstractmethod
    def get_name(self):
        """
        Get user name
        :return: name as string
        """

    @abstractmethod
    def get_age(self):
        """
        Get user age
        :return: age as int
        """

    @abstractmethod
    def get_bank_info(self):
        """
        Get user bank info
        :return: bank info as BankInfo
        """

    @abstractmethod
    def get_budget_list(self):
        """
        Get budget list
        :return: budget list as list of budgets
        """

    @abstractmethod
    def set_name(self, value):
        """
        Set user name
        :param value:name as string
        :return: None
        """

    @abstractmethod
    def set_age(self, value):
        """
        Set user age
        :param value: age as int
        :return: None
        """

    @abstractmethod
    def set_bank_info(self, value):
        """
        Set user Bank info
        :param value: bank info as BankInfo
        :return: None
        """

    @abstractmethod
    def set_budget_list(self, value):
        """
        Set budget list
        :param value: budget list as list of budgets
        :return: None
        """
