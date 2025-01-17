from typing import Any


def check_number(*args: Any):

    '''
Check if the arguments provided are integers.
    '''

    if not args:
        raise AssertionError("No arguments provided")
    for arg in args:
        if not isinstance(arg, (int)):
            raise ValueError(f"Expected int, got {type(arg)}")


def check_dict(**kwargs: Any):

    '''
Check if the keyword arguments provided are valid operations.
    '''

    if not kwargs:
        raise AssertionError("No keyword arguments provided")
    for key, value in kwargs.items():
        if not get_operations_type(value):
            raise ValueError(f"<{value}> is not a valid operation")


def get_operations_type(operation: str):

    '''
Return the type of operation as an integer that will be used
to identify the operation to be performed in the ft_statistic function.

::operation: str:: operation to be performed

::return: int:: type of operation
1: mean
2: median
3: quartile
4: var
5: std
0: unknown operation
    '''

    if (operation == 'mean'):
        return 1
    elif (operation == 'median'):
        return 2
    elif (operation == 'quartile'):
        return 3
    elif (operation == 'var'):
        return 4
    elif (operation == 'std'):
        return 5
    else:
        return 0


def do_mean(values: list):

    '''
Print the mean of the values provided.
    '''

    mean = sum(values) / len(values)
    print(f"mean: {mean}")


def do_median(values: list):

    '''
Print the median of the values provided.
    '''

    n = len(values)
    if n % 2 == 0:
        median = (values[n // 2 - 1] + values[n // 2]) / 2
    else:
        median = values[n // 2]
    print(f"median: {median}")


def do_quartile(values: list):

    '''
Print the quartile of the values provided.
    '''

    n = len(values)
    if n % 2 == 0:
        q1 = float(values[n // 4])
        q3 = float(values[3 * n // 4])
    else:
        q1 = float(values[n // 4])
        q3 = float(values[3 * n // 4])
    print(f"quartile: [{q1}, {q3}]")


def do_var(values: list):

    '''
Print the variance of the values provided.
    '''

    mean = sum(values) / len(values)
    var = sum((x - mean) ** 2 for x in values) / len(values)
    print(f"var: {var}")


def do_std(values: list):

    '''
Print the standard deviation of the values provided.
    '''

    mean = sum(values) / len(values)
    var = sum((x - mean) ** 2 for x in values) / len(values)
    std = var ** 0.5
    print(f"std: {std}")


def manage_operation(values: list, operations: list):

    '''
Perform the operations on the values provided.

::values: list:: list of values
::operations: list:: list of operations
    '''

    for operation in operations:
        if get_operations_type(operation) == 1:
            do_mean(values)
        elif get_operations_type(operation) == 2:
            do_median(values)
        elif get_operations_type(operation) == 3:
            do_quartile(values)
        elif get_operations_type(operation) == 4:
            do_var(values)
        elif get_operations_type(operation) == 5:
            do_std(values)
        else:
            raise Exception("Unknown operation")


def ft_statistics(*args: Any, **kwargs: Any):

    '''
Print the result of the operations on the values provided.

::args: Any:: list of values
::kwargs: Any:: list of operations
    '''

    try:
        check_number(*args)
        check_dict(**kwargs)
    except ValueError as e:
        print(f"[VALUE_ERROR]: {e}")
        return
    except AssertionError as e:
        print(f"[ASSERTION_ERROR]: {e}")
        return

    try:
        values = list(args)
        values.sort()
        operations = list(kwargs.values())
        manage_operation(values, operations)
    except Exception as e:
        print(f"[ERROR]: {e}")
        return
