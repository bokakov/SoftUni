names_of_coffees_nc = input().split()
commands_nc = int(input())


def correct_idx_nc(index):
    if 0 <= index < len(names_of_coffees_nc):
        return True


def include_nc(coffee_nc):
    names_of_coffees_nc.append(coffee_nc)


def remove_nc(first_last_nc, num_coffees_nc):
    global names_of_coffees_nc
    if 0 <= num_coffees_nc < len(names_of_coffees_nc):
        if "first" in first_last_nc:

            for coffee_remove_nc in range(num_coffees_nc):
                names_of_coffees_nc.remove(names_of_coffees_nc[0])
        elif "last" in first_last_nc:

            for coffee_remove_nc in range(num_coffees_nc):
                names_of_coffees_nc.remove(names_of_coffees_nc[-1])


def prefer_nc(coffee_idx_1_nc, coffee_idx_2_nc):
    if correct_idx_nc(coffee_idx_1_nc) and correct_idx_nc(coffee_idx_2_nc):
        names_of_coffees_nc[coffee_idx_1_nc], names_of_coffees_nc[coffee_idx_2_nc] = \
            names_of_coffees_nc[coffee_idx_2_nc], names_of_coffees_nc[coffee_idx_1_nc]


def reverse_nc():
    global names_of_coffees_nc
    names_of_coffees_nc = names_of_coffees_nc[::-1]


for command_nc in range(commands_nc):
    input_command_nc = input().split()
    if "Include" in input_command_nc:
        include_nc(input_command_nc[-1])
    elif "Reverse" in input_command_nc:
        reverse_nc()
    else:
        command_type_nc, idx_1_nc, idx_2_nc = [int(x) if x.isdigit() else x for x in input_command_nc]
        if "Remove" in command_type_nc:
            remove_nc(idx_1_nc, idx_2_nc)
        else:
            prefer_nc(idx_1_nc, idx_2_nc)

print(f"Coffees:\n{' '.join(names_of_coffees_nc)}")
