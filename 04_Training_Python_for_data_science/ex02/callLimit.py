from typing import Any, Callable


def callLimit(limit: int) -> Callable:

    if not isinstance(limit, int):
        raise AssertionError("Limit must be an integer")
    if limit < 0:
        raise AssertionError("Limit must be a positive integer")

    def callLimiter(function: Callable) -> Callable:
        count = 0

        def limit_function(*args: Any, **kwds: Any) -> Any:
            nonlocal count
            if count >= limit:
                raise Exception(
                    f"<function {function.__name__} at {hex(id(function))}> "
                    "call too many times"
                )
            count += 1
            return function(*args, **kwds)

        return limit_function
    return callLimiter
