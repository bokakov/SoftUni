list_1 = input().split(", ")
list_2 = input().split(", ")

result = []

for sub_str in list_1:
    for word in list_2:
        correct_sub_str = sub_str in word
        if correct_sub_str:
            result.append(sub_str)
            break

print(result)
