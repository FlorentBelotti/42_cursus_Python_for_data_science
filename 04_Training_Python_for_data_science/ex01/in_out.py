def square(x: int | float) -> int | float:

    '''Return the square of a number'''

    return x * x


def pow(x: int | float) -> int | float:

    '''Return the power of a number'''

    return x ** x


def outer(x: int | float, function) -> object:

    '''
    Return a function that will apply the function passed as argument
    to the result of the previous call

    ::param x: int | float
    ::param function: function
    ::return: first class function
    '''

    result = x

    def inner() -> float:
        nonlocal result
        result = function(result)
        return result

    return inner
