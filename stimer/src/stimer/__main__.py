import sys

import stimer


class ArgumentError(ValueError):
    pass


def main():
    print("Hello!")

    arguments = sys.argv[1:]
    print(f"Arguments are: {arguments}")
    if len(arguments) != 1:
        raise ArgumentError("Invalid arguments length.")
        exit(1)

    argument = arguments[0]
    print(f"Argument is {argument}.")
    if argument == "on":
        starting = True
    elif argument == "off":
        starting = False
    else:
        raise ArgumentError("Invalid argument. (on/off)")
        exit(1)

    stimer.main(starting)

    print("Done.")


main()
