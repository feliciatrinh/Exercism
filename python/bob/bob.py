import re

"""
.upper() == hey_bob doesn't work because of strings like "4?"
If you can't use isupper then, extract out all the letters somehow
and check if that's not None and also all uppercase?

could have used endswith("?") to avoid out of index
"""

def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob == "":
        reply = "Fine. Be that way!"
    elif hey_bob[-1] == "?" and hey_bob.isupper():
        reply = "Calm down, I know what I'm doing!"
    elif hey_bob[-1] == "?":
        reply = "Sure."
    elif hey_bob.isupper():
        reply = "Whoa, chill out!"
    else:
        reply = "Whatever."
    return reply

def response_regex(hey_bob):
    hey_bob = hey_bob.strip()
    letters = "".join(re.findall(r"[a-zA-Z]", hey_bob))
    if hey_bob == "":
        reply = "Fine. Be that way!"
    elif hey_bob[-1] == "?" and letters != "" and letters == letters.upper():
        reply = "Calm down, I know what I'm doing!"
    elif hey_bob[-1] == "?":
        reply = "Sure."
    elif letters != "" and letters == letters.upper():
        reply = "Whoa, chill out!"
    else:
        reply = "Whatever."
    return reply

def response_better(hey_bob):
    hey_bob = hey_bob.strip()
    is_uppercase = hey_bob.isupper()
    is_question = hey_bob.endswith("?")
    if hey_bob == "":
        reply = "Fine. Be that way!"
    elif is_question and is_uppercase:
        reply = "Calm down, I know what I'm doing!"
    elif is_question:
        reply = "Sure."
    elif is_uppercase:
        reply = "Whoa, chill out!"
    else:
        reply = "Whatever."
    return reply
