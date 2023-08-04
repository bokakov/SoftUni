import re

text = input()

matches = re.findall(r"\s([A-Za-z0-9][\w\-.]*[A-Za-z]@[A-Za-z\-]*[A-Za-z](\.[A-Za-z][A-Za-z\-]*[A-Za-z])+)", text)
print("\n".join([groups[0] for groups in matches]))
