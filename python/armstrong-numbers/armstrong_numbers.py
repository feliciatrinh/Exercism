"""
We want number as an iterable, so cast it into a string.
As you iterate through the string, cast each digit into an int
raise it to the len of the string
and sum each result
"""

def is_armstrong_number(number):
    number_str = str(number)
    num_digits = len(number_str)
    total = sum([int(digit) ** num_digits for digit in number_str])
    return total == number
