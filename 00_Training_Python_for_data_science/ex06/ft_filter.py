def ft_filter(function, iterable):

    """
    Custom implementation of the built-in filter function.

    :param function: takes one argument and returns True or False.
    :param iterable: An iterable to be filtered.
    :return: An iterator with elements for which the function returns True.
    """

    return (item for item in iterable if function(item))
