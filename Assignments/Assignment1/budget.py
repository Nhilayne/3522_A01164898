class Budget:
    """
    Store values for a budget
    """
    def __init__(self, budget_type, budget_target):
        """
        Budget Constructor
        :param budget_type: Name of the budget as string
        :param budget_target: Upper limit of the budget as float
        """
        self._budget_type = budget_type
        self._locked = False
        self._budget_spent = 0.00
        self._budget_target = budget_target
        self._budget_remaining = budget_target

    def get_budget_type(self):
        """
        Get budget type
        :return: string
        """
        return self._budget_type

    def get_locked(self):
        """
        Get locked boolean
        :return: boolean
        """
        return self._locked

    def get_budget_target(self):
        """
        Get Budget limit
        :return: float
        """
        return self._budget_target

    def get_budget_spent(self):
        """
        Get budget spent
        :return: float
        """
        return self._budget_spent

    def set_budget_type(self, value):
        """
        Set budget type
        :param value: Budget name as string
        :return: None
        """
        self._budget_type = value

    def set_locked(self, value):
        """
        Set locked
        :param value: locked as boolean
        :return: None
        """
        self._locked = value

    def set_budget_target(self, value):
        """
        Set budget limit and update remaining budget balance
        :param value: budget limit as float
        :return: None
        """
        self._budget_target = value
        self.update_budget_remaining()

    def set_budget_spent(self, value):
        """
        Set budget spent and update remaining budget balance
        :param value: budget spent as float
        :return: None
        """
        self._budget_spent = value
        self.update_budget_remaining()

    def update_budget_remaining(self):
        """
        Updates remaining budget balance
        :return: None
        """
        self._budget_remaining = self._budget_target - self._budget_spent

    def get_budget_remaining(self):
        """
        Get budget balance remaining
        :return: float
        """
        return self._budget_remaining
