heroes_nc = {}

while True:
    command_nc = input()

    if command_nc == "End":
        break
    command_args_nc = command_nc.split(" ")
    command_nc = command_args_nc[0]

    if command_nc == "Enroll":
        name_nc = command_args_nc[1]
        if name_nc in heroes_nc:
            print(f"{name_nc} is already enrolled.")
        else:
            heroes_nc[name_nc] = ""

    elif command_nc == "Learn":
        name_nc = command_args_nc[1]
        spell_nc = command_args_nc[2]
        if name_nc not in heroes_nc:
            print(f"{name_nc} doesn't exist.")
        else:
            if spell_nc in heroes_nc[name_nc]:
                print(f"{name_nc} has already learnt {spell_nc}.")
            else:
                heroes_nc[name_nc] += f"{spell_nc}"

    elif command_nc == "Unlearn":
        name_nc = command_args_nc[1]
        spell_nc = command_args_nc[2]
        if name_nc not in heroes_nc:
            print(f"{name_nc} doesn't exist.")
        else:
            if spell_nc not in heroes_nc[name_nc]:
                print(f"{name_nc} doesn't know {spell_nc}.")
            else:
                heroes_nc[name_nc] = heroes_nc[name_nc].replace(spell_nc, "")

print("Heroes:")
for (name_nc, spell_nc) in heroes_nc.items():
    for i in range(len(spell_nc)):
        if spell_nc[i].isupper():
            spell_nc = spell_nc[i:] + " " + spell_nc[:i]
    print(f"== {name_nc}: {spell_nc}")
