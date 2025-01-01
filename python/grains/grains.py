def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number - 1)


def total_naive():
    return sum([square(num) for num in range(1, 65)])


# uses the sum of a geometric sequence
# S = a * (r^k - 1) / (r - 1)
# where a is the first term
# r is the ratio
# k is the number of terms
def total():
    return (2**64 - 1)
