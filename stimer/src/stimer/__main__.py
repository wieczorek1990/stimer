import sys

import stimer
from exceptions import ArgumentError


def main():
    print("Hello!")

    arguments = sys.argv[1:]
    print(f"Arguments are: {arguments}")
    if len(arguments) != 2:
        raise ArgumentError("Invalid arguments length.")
        exit(1)

    log_path = arguments[0]
    argument = arguments[1]
    print(f"Argument is {argument}.")
    if argument == "on":
        starting = True
    elif argument == "off":
        starting = False
    else:
        raise ArgumentError("Invalid argument. (on/off)")
        exit(1)

    stimer.main(log_path, starting)

    print("Done.")


main()
