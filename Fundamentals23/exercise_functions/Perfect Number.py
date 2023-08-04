number = int(input())


def check_perfect_number(num):
    check_num = 0
    for i in range(1, num):
        if num % i == 0:
            check_num = check_num + i
    if check_num == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


print(check_perfect_number(number))
