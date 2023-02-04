def sum_first_second(a, b):
    return a + b


def sub_num3(a, b):
    return a - b


num1 = int(input())
num2 = int(input())
num3 = int(input())

sum_result = sum_first_second(num1, num2)
sub_result = sub_num3(sum_result, num3)

print(sub_result)
