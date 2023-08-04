odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    ascii_name_sum = sum(ord(i) for i in input()) // row
    if ascii_name_sum % 2 == 0:
        even_set.add(ascii_name_sum)
    else:
        odd_set.add(ascii_name_sum)

if sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")
