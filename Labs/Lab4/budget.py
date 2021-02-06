class Budget:
    """
    Store values for a budget
    """
    def __init__(self, budget_type, budget_target):
        """
        Budget Constructor
        :param budget_type: Name of the budget
        :param budget_target: Upper limit of the budget
        """
        self._budget_type = budget_type
        self._locked = False
        self._budget_spent = 0.00
        self._budget_target = budget_target

    def get_budget_type(self):
        return self._budget_type()

    def get_locked(self):
        return self._locked

    def get_budget_target(self):
        return self._budget_target

    def get_budget_spent(self):
        return self._budget_target

    def set_budget_type(self, value):
        self._budget_type = value

    def set_locked(self, value):
        self._locked = value

    def set_budget_target(self, value):
        self._budget_target = value

    def set_budget_spent(self, value):
        self._budget_spent = value
