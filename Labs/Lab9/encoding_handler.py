from handler import Handler
from des import DesKey


class EncodingHandler(Handler):

    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_next(self, handler):
        self.next_handler = handler

    def handle(self, request) -> bool:
        encoding_key = DesKey(bytes(request.key, "utf8"))
        if request.data_input is not None:
            request.result = encoding_key.encrypt(bytes(request.data_input, "utf8"), padding=True)
        elif request.input_file is not None:
            file = open(request.input_file, "r")
            request.result = encoding_key.encrypt(bytes(file.read(), "utf8"), padding=True)
            file.close()
        if not self.next_handler:
            return True
        return self.next_handler.handle(request)
