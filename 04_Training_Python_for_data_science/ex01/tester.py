from in_out import outer
from in_out import square
from in_out import pow


def main():
    try:
        my_counter = outer(3, square)
        print(my_counter())
        print(my_counter())
        print(my_counter())
        print("---")
        another_counter = outer(1.5, pow)
        print(another_counter())
        print(another_counter())
        print(another_counter())
        print("---")
        # error_counter = outer("hello", 1)
        # print(error_counter())
        # print(square("hello"))
    except TypeError as e:
        print(f'TypeError: {e}')


if __name__ == "__main__":
    main()
