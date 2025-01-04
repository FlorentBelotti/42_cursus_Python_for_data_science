from ft_filter import ft_filter as ft_filter
import sys


def main():

    """
    Entry point to the program,
    handle test and error.
    """

    try:

        if len(sys.argv) != 3:
            raise AssertionError("[USAGE]: ./filterstring.py <String> <iNt>")

        S = sys.argv[1]
        if not isinstance(S, str):
            raise AssertionError("[ERROR]: <S> is not a string")

        try:
            N = int(sys.argv[2])
        except ValueError:
            raise AssertionError("[ERROR]: <N> is not an int")

    except AssertionError as e:
        print(f"AssertionError: {e}")

    words = S.split()

    filtered_word = list(ft_filter(lambda word: len(word) > N, words))

    print(filtered_word)


if __name__ == "__main__":
    main()
