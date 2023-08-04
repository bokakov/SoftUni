def smallest_number(numbers):
    min_number = float('inf')
    for num in numbers:
        if num < min_number:
            min_number = num

    return min_number


number1 = int(input())
number2 = int(input())
number3 = int(input())

print(smallest_number([number1, number2, number3]))
