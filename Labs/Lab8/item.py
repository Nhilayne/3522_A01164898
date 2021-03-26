from abc import ABC, abstractmethod


class Item(ABC):

    @abstractmethod
    def get_title(self):
        """
        Returns the title of the book
        :return: a string
        """
        pass

    @abstractmethod
    def increment_number_of_copies(self):
        """
        Increments the number of copies of an item by 1
        """
        pass

    @abstractmethod
    def decrement_number_of_copies(self):
        """
        Decrements the number of copies of an item by 1
        """
        pass

    @abstractmethod
    def get_num_copies(self):
        """
        Returns the number of copies that are available for this
        specific book.
        :return: an int
        """
        pass

    @abstractmethod
    def check_availability(self):
        """
        Returns True if the book is available and False otherwise
        :return: A Boolean
        """
        pass

    @property
    @abstractmethod
    def call_number(self):
        """
        Right, this here is another way of using properties.
        We use decorators. The @property decorator defines a property
        that only allows us to GET a value and not set one.

        I want to point out that I have not expected you to do this in
        your labs. I'm using this as an opportunity to introduce you to
        a new way of avoiding mechanical getters and setters.
        :return:
        """
        pass
