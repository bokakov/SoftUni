x, y = [int(num) for num in input().split()]

first_set = {int(input()) for _ in range(x)}
second_set = {int(input()) for _ in range(y)}

print(*first_set.intersection(second_set), sep="\n")
