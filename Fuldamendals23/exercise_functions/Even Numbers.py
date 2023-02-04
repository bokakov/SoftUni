def even(num):
    result = num % 2 == 0
    return result


numbers = [int(x) for x in input().split()]

print(list(filter(even, numbers)))
