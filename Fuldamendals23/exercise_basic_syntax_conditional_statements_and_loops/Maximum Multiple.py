divisor = int(input())
max_number = int(input())

result = 0
for num in range(1, max_number + 1):
    if num % divisor == 0:
        result = num

print(result)
