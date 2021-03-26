from book import Book
from dvd import DVD
from journal import Journal


class LibraryItemGenerator:
    def __init__(self):
        self._title = input("Enter a title: ")
        self._call_num = input("Enter a call number: ")
        self._num_copies = input("Enter number of copies: ")

    def create_item(self):
        item_type = input("Enter an item type:\n1: Book\n2: Dvd\n3: Journal")
        item = "invalid input given"
        if item_type == "1":
            item = Book(self._title, input("Enter Authour name: "), self._call_num, self._num_copies)
        elif item_type == "2":
            item = DVD(self._title, input("Enter Release Date: "), input("Enter Region Code: "),\
                       self._call_num, self._num_copies)
        elif item_type == "3":
            item = Journal(self._title, input("Enter Issue Number: "), input("Enter Publisher Name: "), self._call_num, self._num_copies)
        return item
