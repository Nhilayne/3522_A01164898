from handler import Handler
from os import path


class FileHandler(Handler):

    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_next(self, handler):
        self.next_handler = handler

    def handle(self, request) -> bool:
        print("Validating File")
        if request.input_file is None or (path.isfile(request.input_file) and request.data_input is None):
            print("Valid File")
            if not self.next_handler:
                return True
            return self.next_handler.handle(request)
        else:
            return False
