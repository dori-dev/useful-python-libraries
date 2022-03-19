"""doctest library"""
import doctest


def fib(n: int):
    """Calculates the n-th Fibonacci number iteratively
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(6)
    8
    >>> fib(10)
    55
    >>> fib(15)
    610
    """
    first, second = 0, 1
    for _ in range(n):
        first, second = second, first + second
    return first


if __name__ == "__main__":
    doctest.testmod()
