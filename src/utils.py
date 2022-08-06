

def build_header(params: list, space: int) -> str:
    """ This method takes a list of parameters as strings and build a table header """

    header = ""
    for param in params:
        header += f"{param : >{space}}"

    header = header + "\n"

    return header
