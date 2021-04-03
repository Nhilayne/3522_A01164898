from handler import Handler


class KeyHandler(Handler):

    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_next(self, handler):
        self.next_handler = handler

    def handle(self, request) -> bool:
        print("Validating Key")
        if len(request.key) == 8 or len(request.key) == 16 or len(request.key) == 24:
            print("Valid length 8,16,or 24")
            if not self.next_handler:
                return True
            return self.next_handler.handle(request)
        else:
            return False
