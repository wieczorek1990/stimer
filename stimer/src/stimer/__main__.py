import sys

import stimer
from exceptions import ArgumentError


def main():
    arguments = sys.argv[1:]
    if len(arguments) != 2:
        raise ArgumentError("Invalid arguments length.")
        exit(1)

    log_path = arguments[0]
    argument = arguments[1]
    if argument == "on":
        starting = True
    elif argument == "off":
        starting = False
    else:
        raise ArgumentError("Invalid argument. (on/off)")
        exit(1)

    stimer.main(log_path, starting)


main()
