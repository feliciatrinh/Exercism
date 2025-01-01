LETTERS_TO_INDEX = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
           'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
           'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21,
           'w': 22, 'x': 23, 'y': 24, 'z': 25
           }
INDEX_TO_LETTERS = dict(zip(LETTERS_TO_INDEX.values(), LETTERS_TO_INDEX.keys()))

def rotate_one(text, key):
    rotations = key % 26
    cipher = ""
    for character in text:
        lowered = character.lower()
        if lowered in LETTERS_TO_INDEX:
            new_index = (LETTERS_TO_INDEX[character.lower()] + rotations) % 26
            new_letter = INDEX_TO_LETTERS[new_index]
            cipher += new_letter if character.islower() else new_letter.upper()
        else:
            cipher += character

    return cipher


# this works because key is always between 0 and 26
CHARS = "abcdefghijklmnopqrstuvwxyz"
def rotate(text, key):
    newchars = CHARS[key:] + CHARS[:key]
    trans = str.maketrans(CHARS + CHARS.upper(), newchars + newchars.upper())
    return text.translate(trans)
