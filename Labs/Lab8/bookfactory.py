from book import Book


class BookFactory:

    @staticmethod
    def create():
        title = input("Enter a title: ")
        call_num = input("Enter a call number: ")
        num_copies = input("Enter number of copies: ")
        author = input("Enter an author: ")
        return Book(title=title, call_num=call_num, num_copies=num_copies, author=author)
