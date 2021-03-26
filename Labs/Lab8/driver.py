from library import Library
from book import Book

def generate_test_books():
    """
    Return a list of books with dummy data.
    :return: a list
    """
    book_list = [
        Book("Harry Potter 1", "J K Rowling", "100.200.300", 2),
        Book("Harry Potter 2", "J K Rowling", "999.224.854", 5),
        Book("Harry Potter 3", "J K Rowling", "631.495.302", 4),
        Book("The Cat in the Hat", "Dr. Seuss", "123.02.204", 1)
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
