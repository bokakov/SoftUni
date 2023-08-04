from collections import deque

string_expression = input().split()

numbers = deque()

for el in string_expression:
    if el in "+-*/":
        while len(numbers) > 1:
            num_one = numbers.popleft()
            num_two = numbers.popleft()

            result = 0

            if el == "+":
                result = num_one + num_two
            elif el == "-":
                result = num_one - num_two
            elif el == "*":
                result = num_one * num_two
            else:
                result = num_one // num_two
            numbers.appendleft(result)
    else:
        numbers.append(int(el))

print(numbers.popleft())
