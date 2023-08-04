text = input().split("|")

sub_list = []

for sub_str in text[::-1]:
    sub_list.extend(sub_str.split())

print(*sub_list)
