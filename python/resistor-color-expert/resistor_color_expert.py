RESISTANCE_MAPPING = {
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

TOLERANCE_MAPPING = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%"
}


def resistor_label(colors):
    if len(colors) == 1:
        label = "0 ohms"
    else:
        colors, multiplier_color, tolerance_color = colors[:-2], colors[-2], colors[-1]
        multiplier = RESISTANCE_MAPPING[multiplier_color]
        tolerance = TOLERANCE_MAPPING[tolerance_color]
        digits = int("".join([str(RESISTANCE_MAPPING[color]) for color in colors]))
        number = digits * 10 ** multiplier
        if number >= 10 ** 9:
            prefix = "giga"
            number /= 10 ** 9
        elif number >= 10 ** 6:
            prefix = "mega"
            number /= 10 ** 6
        elif number >= 10 ** 3:
            prefix = "kilo"
            number /= 10 ** 3
        else:
            prefix = ""

        label = f"{number:g} {prefix}ohms ±{tolerance}"

    return label
