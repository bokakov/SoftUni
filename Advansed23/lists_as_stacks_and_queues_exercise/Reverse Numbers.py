numbers = input().split()
for num in range(len(numbers)):
    print(f"{numbers.pop()}", end=" ")
