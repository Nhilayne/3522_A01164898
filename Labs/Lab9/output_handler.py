from handler import Handler


class OutputHandler(Handler):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_next(self, handler):
        self.next_handler = handler

    def handle(self, request) -> bool:
        print("Handling Output")

        if request.output != "print":
            file = open(request.output, "w")
            file.write(request.result)
            file.close()
        else:
            print(request.result)

        if not self.next_handler:
            return True
        return self.next_handler.handle(request)
