import re

def is_valid_one(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False

    multiplier = 10
    sum_products = 0
    for letter in isbn:
        if letter == 'X' and multiplier == 1:
            digit = 10
        else:
            try:
                digit = int(letter)
            except:
                return False
        sum_products += digit * multiplier
        multiplier -= 1

    return sum_products % 11 == 0


def is_valid_two(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10 or re.findall(r'[^0-9]', isbn[:-1]) or (re.match(r'[^0-9]', isbn[-1]) and isbn[-1] != 'X'):
        return False

    multiplier = 10
    sum_products = 0
    for letter in isbn:
        if letter == 'X':
            digit = 10
        else:
            digit = int(letter)
        sum_products += digit * multiplier
        multiplier -= 1

    return sum_products % 11 == 0

def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10 or not all([d.isdigit() for d in isbn[:-1]]) or (not isbn[-1].isdigit() and isbn[-1] != 'X'):
        return False

    multiplier = 10
    sum_products = 0
    for letter in isbn:
        if letter == 'X':
            digit = 10
        else:
            digit = int(letter)
        sum_products += digit * multiplier
        multiplier -= 1

    return sum_products % 11 == 0
