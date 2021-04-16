import argparse
from request import Request
from pokefacade import PokeFacade




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
    parser.add_argument("category", choices=['pokemon', 'ability', 'move'], help="pokemon, ability, or move to query")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--inputfile", dest="file_name")
    group.add_argument("--inputdata", dest="input")
    parser.add_argument("-e", "--expanded", action='store_true', help="indicate that output should be expanded")
    parser.add_argument("-o", "--output", default="print", help="The output of the program. This is 'print' by default,"
                                                                " but can be set to a file name as well.")
    try:
        args = parser.parse_args()
        request = Request()
        request.category = args.category
        request.input_file = args.file_name
        request.input = args.input
        request.extended = args.expanded
        request.output = args.output
        # print(request)
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


def main(request: Request):
    facade = PokeFacade()
    output = facade.execute_request(request)
    if request.output == "print":
        for x in output:
            print(x)
    else:
        file = open(request.output, "w")
        for x in output:
            file.write(str(x))
        file.close()


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
