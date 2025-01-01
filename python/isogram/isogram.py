import re

NOT_COUNTED = [' ', '-']

def is_isogram(string):
    lowered = string.lower()
    letters = ''.join(re.findall(r'[a-z]*', lowered))
    return len(letters) == len(set(letters))


def is_isogram_dict(string):
    letters = {}
    for letter in string.lower():
        if letter not in NOT_COUNTED:
            if letter in letters:
                return False
            else:
                letters[letter] = 1
    return True
