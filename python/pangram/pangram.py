import re

def is_pangram(sentence):
    lowered = sentence.lower()
    only_letters = ''.join(re.findall(r'[a-z]*', lowered))
    return len(set(only_letters)) == 26

# another possible solution
from string import ascii_lowercase
def is_pangram(s):
    return all(c in s.lower() for c in ascii_lowercase)

# another possible solution

from string import ascii_lowercase
ALPHABET = set(ascii_lowercase)
def is_pangram(string):
    return ALPHABET.issubset(string.lower())
