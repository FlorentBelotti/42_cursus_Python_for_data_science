import sys


def main():

    """
    Entry point to the program,
    handle test and error.
    """

    NESTED_MORSE = {
        "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
        "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ",
        "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
        "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
        "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
        "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
        "8": "---.. ", "9": "----. ",
        " ": "/ "
    }

    try:

        if len(sys.argv) != 2:
            raise AssertionError("[USAGE]: ./sos.py <string>")

        morse_code = ""

        for char in sys.argv[1]:
            if NESTED_MORSE[char.upper()]:
                morse_code += NESTED_MORSE[char.upper()]
            else:
                raise ValueError(f"[ERROR]: Char '{char}' not found in morse")

        print(morse_code.strip())

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")


if __name__ == "__main__":
    main()
