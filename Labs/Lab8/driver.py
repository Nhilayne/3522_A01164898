from library import Library
from book import Book


def generate_test_books():
    """
    Return a list of books with dummy data.
    :return: a list
    """
    book_list = [
        Book(title="Harry Potter 1", author="J K Rowling", call_num="100.200.300", num_copies=2),
        Book(title="Harry Potter 2", author="J K Rowling", call_num="999.224.854", num_copies=5),
        Book(title="Harry Potter 3", author="J K Rowling", call_num="631.495.302", num_copies=4),
        Book(title="The Cat in the Hat", author="Dr. Seuss", call_num="123.02.204", num_copies=1)
    ]
    return book_list


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """
    book_list = generate_test_books()
    my_epic_library = Library(book_list)
    my_epic_library.display_library_menu()


if __name__ == '__main__':
    main()
