special_mats = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

legendary_item_by_mat = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

junk = {}

crafted = False
while not crafted:
    command = input()
    materials = command.split()

    for idx in range(0, len(materials) - 1, 2):
        quantity = int(materials[idx])
        material = materials[idx + 1].lower()

        if material in special_mats:
            special_mats[material] += quantity
            if special_mats[material] >= 250:
                special_mats[material] -= 250
                crafted = True
                print(f"{legendary_item_by_mat[material]} obtained!")
                break
        else:
            if material in junk:
                junk[material] += quantity
            else:
                junk[material] = quantity
for material, count in special_mats.items():
    print(f"{material}: {count}")

for material, count in junk.items():
    print(f"{material}: {count}")
