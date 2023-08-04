from collections import deque

material_box = deque(int(x) for x in input().split())
magic_value = deque(int(x) for x in input().split())

crafted = []
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while material_box and magic_value:
    material = material_box.pop() if magic_value[0] or not material_box[0] else 0
    magic_level = magic_value.popleft() if material or not magic_value[0] else 0

    if not magic_level:
        continue
    product = material * magic_level

    if presents.get(product):
        crafted.append(presents[product])
    elif product < 0:
        material_box.append(material + magic_level)
    elif product > 0:
        material_box.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if material_box:
    print(f"Materials left: {', '.join([str(x) for x in material_box][::-1])}")
if magic_value:
    print(f"Magic left: {', '.join([str(x) for x in magic_value])}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]