import math
import time
import functools


"""
function which returns the average of any number of given parameters
"""


def average(*args: float) -> float:
    return sum(args) / len(args)


x = average(20, 50, 66, 32)
print(x)


"""
Lucas numbers, timer and memoize decorators
"""


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"{func.__name__!r} finished in {elapsed_time:.4f} seconds.")
        return value

    return wrapper


# use decorator "timer" to show elapsed time
# timer

# use decorator memoize for much faster calculations
@memoize
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


print(lucas(100))


# prime factorization of a number
def primes(n):
    while n % 2 == 0:
        print(2),
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            print(i),
            n = n / i
    if n > 2:
        print(n)


x = 20633239
primes(x)
