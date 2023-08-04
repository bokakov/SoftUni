import re

result = []
while True:
    line = input()
    if not line:
        break

    matches = re.findall("\\d+", line)
    result.extend(matches)

print(" ".join(result))
