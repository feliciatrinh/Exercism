MAPPING = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

def get_units_power(zeros):
    if zeros < 3:
        units = "ohms"
        power = 0
    elif zeros < 6:
        units = "kiloohms"
        power = 3
    elif zeros < 9:
        units = "megaohms"
        power = 6
    elif zeros < 12:
        units = "gigaohms"
        power = 9
    return units, power

def label_one(colors):
    number = int(f"{MAPPING[colors[0]]}{MAPPING[colors[1]]}{'0' * MAPPING[colors[2]]}")
    zeros = 0
    num = number
    while num > 0 and num % 10 == 0:
        num = num // 10
        zeros += 1

    units, power = get_units_power(zeros)

    return f"{number // 10 ** power} {units}"

def label_two(colors):
    num = int(f"{MAPPING[colors[0]]}{MAPPING[colors[1]]}")
    if num > 0 and num % 10 == 0:
        zeros = MAPPING[colors[2]] + 1
        num = num // 10
    else:
        zeros = MAPPING[colors[2]]

    units, power = get_units_power(zeros)
    zeros -= power
    return f"{num}{'0' * zeros} {units}"

def label(colors):
    number = int(f"{MAPPING[colors[0]]}{MAPPING[colors[1]]}{'0' * MAPPING[colors[2]]}")
    if number >= 10 ** 9:
        prefix = "giga"
        number //= 10 ** 9
    elif number >= 10 ** 6:
        prefix = "mega"
        number //= 10 ** 6
    elif number >= 10 ** 3:
        prefix = "kilo"
        number //= 10 ** 3
    else:
        prefix = ""

    return f"{number} {prefix}ohms"
