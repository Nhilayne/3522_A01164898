from Labs.Lab5.file_handler import FileHandler
from pathlib import Path


class Dictionary:
    """
    Dictionary class
    """
    def __init__(self, out_path):
        """
        Stores data about dictionary
        :param out_path: query output file filepath
        """
        self._out_path = out_path
        self._is_loaded = False
        self._dictionary = None

    def get_is_loaded(self):
        """
        is_loaded getter
        :return: is_loaded
        """
        return self._is_loaded

    def load_dictionary(self, filepath):
        """
        Loads dictionary from file at filepath
        :param filepath:
        :return: None
        """
        extension = Path(filepath).suffix
        self._dictionary = FileHandler.load_data(filepath, extension)
        self._is_loaded = True

    def query_definition(self, key):
        """
        Searches for key in dictionary and returns it's definition(s) if found
        :param key: search term
        :return: definition of search term or "key not found" if not found
        """
        search_key = key.lower()
        for dict_key in self._dictionary.keys():
            if str(dict_key).lower() == search_key:
                print("Key found")
                FileHandler.write_lines(self._out_path, [dict_key, self._dictionary[dict_key]])
                return self._dictionary[dict_key]
        print("Key not found")
        return "Key not found"


def main():
    """
    Main driver of the program
    :return: none
    """
    while True:
        in_path = input("Please enter the dictionary file path: ")
        if Path(in_path).is_file():
            break
        else:
            print("Invalid file path")
    out_path = input("Please enter the output file path: ")
    dictionary = Dictionary(out_path)
    dictionary.load_dictionary(in_path)
    while True:
        print("Please enter a word or phrase to search for: ")
        print("Enter 'exitprogram' to quit")
        search_term = input()
        if search_term.lower() == "exitprogram":
            break
        else:
            dictionary.query_definition(search_term)


if __name__ == '__main__':
    main()
