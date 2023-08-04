import re

command = input()
regex = re.compile(r">>(\w+)<<(\d+(\.\d+)?)!(\d+)")
names = []
total_price = 0

while command != "Purchase":
    matches = regex.finditer(command)
    for show in matches:
        names.append(show[1])
        total_price += (float(show[2]) * int(show[4]))
    command = input()

print("Bought furniture:")
if names:
    for name in names:
        print(name)
print(f"Total money spend: {total_price:.2f}")
