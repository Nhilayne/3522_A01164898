class Request:

    def __init__(self):
        self.category = None
        self.input_file = None
        self.input = None
        self.extended = None
        self.output = None
        self.result = None

    # def __str__(self):
    #     return f"Request: State: {self.encryption_state}, Data: {self.data_input}" \
    #            f", Input file: {self.input_file}, Output: {self.output}, " \
    #            f"Key: {self.key}"
