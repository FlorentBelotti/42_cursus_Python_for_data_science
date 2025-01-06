def slice_me(family: list, start: int, end: int):
    """
    Slice a 2D array (list of lists) from start to end indices for both rows
    and columns.

    :param family: 2D array (list of lists).
    :param start: Starting index for slicing (inclusive).
    :param end: Ending index for slicing (exclusive).
    :return: Sliced 2D array.
    """

    if not all(isinstance(row, list) for row in family):
        raise ValueError("All elements of the input must be lists")

    if not all(len(row) == len(family[0]) for row in family):
        raise ValueError("All rows must have the same number of columns")

    rows = len(family)
    cols = len(family[0])

    print(f'My shape is : ({rows}, {cols})')

    sliced_family = family[start:end]

    sliced_rows = len(sliced_family)
    sliced_cols = len(sliced_family[0]) if sliced_rows > 0 else 0

    print(f'My new shape is : ({sliced_rows}, {sliced_cols})')

    return sliced_family
