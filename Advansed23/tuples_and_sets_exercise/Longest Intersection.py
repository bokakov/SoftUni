interaction = []

for _ in range(int(input())):
    data = input().split("-")
    first_data = data[0].split(",")
    second_data = data[1].split(",")

    first_set = set(n for n in range(int(first_data[0]), int(first_data[1]) + 1))
    second_set = set(n for n in range(int(second_data[0]), int(second_data[1]) + 1))
    intersection = first_set.intersection(second_set)

    if len(intersection) > len(interaction):
        interaction = list(intersection)

print(f"Longest intersection is {interaction} with length {len(interaction)}")
