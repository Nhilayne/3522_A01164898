from bookfactory import BookFactory
from dvdfactory import DVDFactory
from journalfactory import JournalFactory


class LibraryItemGenerator:

    @classmethod
    def create_item(cls):
        item_type = input("Enter an item type:\n1: Book\n2: Dvd\n3: Journal\n")
        item = "invalid input given"
        if item_type == "1":
            item = BookFactory.create()
        elif item_type == "2":
            item = DVDFactory.create()
        elif item_type == "3":
            item = JournalFactory.create()
        return item
