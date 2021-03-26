""" This module houses the library"""
from catalogue import Catalogue


class Library:
    """
    The Library consists of a list of books and provides an
    interface for users to check out, return and find books.
    """
    def __init__(self, catalogue):
        """
        Intialize the library with a list of books.
        :param catalogue: a list of item objects to create catalogue from.
        """
        self._catalogue = Catalogue(catalogue)

    def display_library_menu(self):
        """
        Display the library menu allowing the user to either access the
        list of books, check out, return, find, add, remove a book.
        """
        user_input = None
        while user_input != 7:
            print("\nWelcome to the Library!")
            print("-----------------------")
            print("1. Display all books")
            print("2. Check Out a book")
            print("3. Return a book")
            print("4. Find a book")
            print("5. Add a book")
            print("6. Remove a book")
            print("7. Quit")
            string_input = input("Please enter your choice (1-7)")

            #handle user pressing only enter in menu
            if(string_input == ''):
                continue

            user_input = int(string_input)

            if user_input == 1:
                self._catalogue.display_available_item()
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                call_number = input("Enter the call number of the book"
                                    " you wish to check out.")
                self._catalogue.check_out(call_number)
            elif user_input == 3:
                call_number = input("Enter the call number of the book"
                                    " you wish to return.")
                self._catalogue.return_item(call_number)
            elif user_input == 4:
                input_title = input("Enter the title of the book:")
                found_titles = self._catalogue.find_items(input_title)
                print("We found the following:")
                if len(found_titles) > 0:
                    for title in found_titles:
                        print(title)
                else:
                    print("Sorry! We found nothing with that title")

            elif user_input == 5:
                self._catalogue.add_item()

            elif user_input == 6:
                call_number = input("Enter the call number of the book")
                self._catalogue.remove_item(call_number)

            elif user_input == 7:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 7.")

        print("Thank you for visiting the Library.")