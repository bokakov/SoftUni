text = input()
result = text[0]

for char in text:
    if char == result[-1]:
        continue
    result += char

print(result)
