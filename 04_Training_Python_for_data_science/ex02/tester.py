from callLimit import callLimit


def main():
    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        try:
            f()
        except Exception as e:
            print(f"Error: {e}")
        try:
            g()
        except Exception as e:
            print(f"Error: {e}")

    try:
        @callLimit(-1)
        def z():
            print("z()")
    except AssertionError as e:
        print(f"Error: {e}")

    try:
        @callLimit("hello")
        def y():
            print("y()")
    except AssertionError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
