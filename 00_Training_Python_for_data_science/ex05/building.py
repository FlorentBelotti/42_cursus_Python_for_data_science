import sys
import string


def building(message):

    """
    Takes a single string argument and displays the sums of
    its upper-case characters, lower-case characters, punctuation
    characters, digits and spaces.
    """

    sums = {
        "sum_of_chara": len(message),
        "sum_of_upper": 0,
        "sum_of_lower": 0,
        "sum_of_punct": 0,
        "sum_of_digit": 0,
        "sum_of_space": 0
    }

    sums["sum_of_upper"] = sum(1 for c in message if c.isupper())
    sums["sum_of_lower"] = sum(1 for c in message if c.islower())
    sums["sum_of_digit"] = sum(1 for c in message if c.isdigit())
    sums["sum_of_space"] = sum(1 for c in message if c.isspace())
    sums["sum_of_punct"] = sum(1 for c in message if c in string.punctuation)

    print(f"The texte contains {sums['sum_of_chara']} characters:")
    print(f"{sums['sum_of_upper']} upper letters")
    print(f"{sums['sum_of_lower']} lower letters")
    print(f"{sums['sum_of_punct']} punctuation marks")
    print(f"{sums['sum_of_space']} spaces")
    print(f"{sums['sum_of_digit']} digits")

def main():

    """
    Entry point to the program,
    handle test and error.
    """

    if len(sys.argv) < 2:
        print("[USAGE]: ./building.py <message>")
    elif len(sys.argv) > 2:
        raise AssertionError("[ERROR]: too many arguments")
    else:
        building(sys.argv[1])


if __name__ == "__main__":
    main()
