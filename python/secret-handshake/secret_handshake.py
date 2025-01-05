def commands_one(binary_str):
    binary_str = binary_str[::-1]
    actions = []
    reverse_flag = False
    for index, digit in enumerate(binary_str):
        if digit == "1":
            if index == 0:
                actions.append("wink")
            elif index == 1:
                actions.append("double blink")
            elif index == 2:
                actions.append("close your eyes")
            elif index == 3:
                actions.append("jump")
            elif index == 4:
                reverse_flag = True

    if reverse_flag:
        actions = actions[::-1]

    return actions


ACTION_MAPPING = {
    0: "wink",
    1: "double blink",
    2: "close your eyes",
    3: "jump"
}

def commands_two(binary_str):
    binary_str = binary_str[::-1]
    actions = []
    reverse_flag = False
    for index, digit in enumerate(binary_str):
        if digit == "1":
            if index < 4:
                actions.append(ACTION_MAPPING[index])
            else:
                reverse_flag = True

    if reverse_flag:
        actions = actions[::-1]

    return actions


ACTIONS = ["wink", "double blink", "close your eyes", "jump"]

def commands(binary_str):
    number = int(binary_str, base=2)
    actions = []
    for index, action in enumerate(ACTIONS):
        if number & 1 << index:
            actions.append(action)

    if number & 1 << 4:
        actions.reverse()
    return actions


# return a binary string given a number between 1 and 31
def number_to_binary(number):
    if number < 1 or number > 31:
        raise ValueError("number must be between 1 and 31")

    binary_str = ""
    def builder(num, x, binary):
        if num >= x:
            binary += "1"
            num -= x
        else:
            binary += "0"
        return num, binary

    for threshold in [16, 8, 4, 2, 1]:
        number, binary_str = builder(number, threshold, binary_str)

    return binary_str


def number_to_binary_two(number):
    if number < 1:
        raise ValueError("number must be greater than or equal to 1")
    binary_str = ""
    power = 0
    while number >= 2 ** power:
        if number & 1 << power:
            binary_str += "1"
        else:
            binary_str += "0"
        power += 1

    return binary_str[::-1]
