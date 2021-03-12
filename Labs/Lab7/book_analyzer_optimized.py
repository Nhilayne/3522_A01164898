import re


class BookAnalyzer:
    """
    This Class provides the ability to store unique words
    from a file in memory, as well as fetch the list of unique
    words.
    """

    def __init__(self):
        self.text = None

    def read_data(self, src="House of Usher.txt"):
        """
        Reads a text file, then assigns a list of all unique
        words to the text class variable
        :param src: text file to read in
        :return: None
        """
        with open(src, mode='r', encoding='utf-8') as book_file:
            text = book_file.read(-1)
        self.text = set(re.split('[*:;,.!?()\[\]\"\'\n\-\s]+', text.lower()))

    def get_unique_words(self):
        """
        Returns list of unique words
        :return: a list of all the unique words.
        """
        return self.text


def main():
    book_analyzer = BookAnalyzer()
    book_analyzer.read_data()
    unique_words = book_analyzer.get_unique_words()
    print("-" * 50)
    print('\n'.join(unique_words))
    print("-" * 50)
    print(f"List of unique words (Count: {len(unique_words)})")
    print("-" * 50)


if __name__ == '__main__':
    main()
