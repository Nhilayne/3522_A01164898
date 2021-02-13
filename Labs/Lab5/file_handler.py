import ast
from enum import Enum
import json


class FileExtensions(Enum):
    """
    Defines Valid File Extensions
    """
    TEXT = ".txt"
    JSON = ".json"


class FileHandler:
    """
    Class responsible for reading and appending to a file
    """
    @staticmethod
    def load_data(path, file_extension):
        """
        Loads and reads a file
        :param path: file path
        :param file_extension: file extension
        :return: contents of file
        """
        if file_extension == FileExtensions.JSON.value:
            with open(path, "r") as json_file:
                contents = json.load(json_file)
                return contents
        elif file_extension == FileExtensions.TEXT.value:
            with open(path, "r") as text_file:
                contents = text_file.read()
                formatted_contents = ast.literal_eval(contents)
                return formatted_contents
        else:
            raise InvalidFileTypeError("File type not supported")

    @staticmethod
    def write_lines(path, lines):
        """
        Loads and appends to a file
        :param path: file path
        :param lines: list of strings to append to file
        :return: None
        """
        file = open(path, "a")
        file.write("Search: " + str(lines[0]))
        file.write("\nDefinition: " + str(lines[1]) + "\n")
        file.close()


class InvalidFileTypeError(Exception):
    """
    Raised when file extension is not supported
    """
