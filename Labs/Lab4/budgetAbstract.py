
class Budget(ABC):
    @abstractmethod
    def get_budget_type(self):
        pass

    @abstractmethod
    def get_locked(self):
        pass

    @abstractmethod
    def get_budget_target(self):
        pass

    @abstractmethod
    def get_budget_spent(self):
        pass

    @abstractmethod
    def set_budget_type(self, value):
        pass

    @abstractmethod
    def set_locked(self, value):
        pass

    @abstractmethod
    def set_budget_target(self, value):
        pass

    @abstractmethod
    def set_budget_spent(self, value):
        pass
