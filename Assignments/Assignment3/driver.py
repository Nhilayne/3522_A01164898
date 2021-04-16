import argparse
from request import Request
from pokefacade import PokeFacade


# class Request:
#
#     def __init__(self):
#         self.category = None
#         self.data_source = None
#         self.extended = None
#         self.output = None
#         self.result = None
#
#     def __str__(self):
#         return f"Request: State: {self.encryption_state}, Data: {self.data_input}" \
#                f", Input file: {self.input_file}, Output: {self.output}, " \
#                f"Key: {self.key}"


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("category", help="pokemon, ability, or move to query")
    parser.add_argument("ds", "datasource", help="source of the data, either a file or name/id")
    parser.add_argument("-e", "--expanded", default="false", help="indicate that output should be expanded")
    parser.add_argument("-o", "--output", default="print", help="The output of the program. This is 'print' by default,"
                                                                " but can be set to a file name as well.")
    try:
        args = parser.parse_args()
        request = Request()
        request.category = args.category
        request.data_source = args.datasource
        request.extended = args.expanded
        request.output = args.output
        print(request)
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()



def main(request: Request):
    facade = PokeFacade()
    output = facade.execute_request(request)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
