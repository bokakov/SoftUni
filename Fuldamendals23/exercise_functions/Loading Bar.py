percent = int(input())


def loading_bar(number):
    number_range = int(number / 10)
    target = 10
    if target == number_range:
        return "100% Complete!\n" + "[" + target * "%" + "]"
    else:
        return f"{number}% " + "[" + number_range * "%" + (target - number_range) * "." + "]\n" + "Still loading..."


print(loading_bar(percent))
