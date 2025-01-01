def reverse(text):
    reversed_text = ""
    for index in range(-1, (len(text) * -1) - 1, -1):
        reversed_text += text[index]

    return reversed_text


# Uses a list to be able to modify in place with less looping
def reverse_list(text):
    text_list = list(text)
    back_index = -1
    for index in range(len(text) // 2):
        front_letter = text_list[index]
        text_list[index] = text_list[back_index]
        text_list[back_index] = front_letter
        back_index -= 1

    return "".join(text_list)


# you can also just return text[::-1]
