from pathlib import Path
import unittest

from Labs.Lab5.file_handler import FileHandler
from Labs.Lab5.dictionary import Dictionary


class TestLoad(unittest.TestCase):
    def test_init(self):
        dictionary = Dictionary(None)
        path = "/Users/Iangs/Desktop/data.json"
        dictionary.load_dictionary(path)
        loaded = dictionary.get_is_loaded()
        self.assertEqual(loaded, True)


class TestWrite(unittest.TestCase):
    def test_init(self):
        path = "/Users/Iangs/Desktop/UnitTestOutput.txt"
        text = ["test", "success"]
        FileHandler.write_lines(path, text)
        file_exists = Path(path).is_file()
        self.assertEqual(file_exists, True)


class TestQuery(unittest.TestCase):
    def test_init(self):
        path = "/Users/Iangs/Desktop/data.json"
        path_out = "/Users/Iangs/Desktop/UnitTestOutput.txt"
        query = "AIDS"
        dictionary = Dictionary(path_out)
        dictionary.load_dictionary(path)
        query_result = dictionary.query_definition(query)
        expected_result = "['A disease of the human immune system caused by the human immunodeficiency virus (HIV).']"
        self.assertEqual(query_result, expected_result)


def main():
    TestLoad()
    TestWrite()
    TestQuery()


if __name__ == '__main__':
    main()
