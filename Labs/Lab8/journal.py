from item import Item


class Journal(Item):
    def __init__(self, **journal):
        self._issue_number = journal['issue_number']
        self._publisher = journal['publisher']
        self._title = journal['title']
        self._call_num = journal['call_num']
        self._num_copies = journal['num_copies']

    def get_publisher(self):
        return self._publisher.publisher()

    def get_issue_number(self):
        return self._issue_number.issue_number()

    def get_title(self):
        """
        Returns the title of the book
        :return: a string
        """
        return self._title.title()

    def increment_number_of_copies(self):
        """
        Increments the number of copies of an item by 1
        """
        self._num_copies += 1

    def decrement_number_of_copies(self):
        """
        Decrements the number of copies of an item by 1
        """
        self._num_copies -= 1

    def get_num_copies(self):
        """
        Returns the number of copies that are available for this
        specific book.
        :return: an int
        """
        return self._num_copies

    def check_availability(self):
        """
        Returns True if the book is available and False otherwise
        :return: A Boolean
        """
        if self._num_copies > 0:
            return True
        else:
            return False

    @property
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
        return self._call_num

    def __str__(self):
        return f"---- Journal: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Publisher: {self._publisher}\n"\
               f"Issue: {self._issue_number}"
