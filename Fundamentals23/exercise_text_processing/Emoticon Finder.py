text = input()

for idx in range(len(text)):
    char = text[idx]
    if char == ":" and idx + 1 < len(text):
        emoji = text[idx + 1]
        print(f":{emoji}")
        idx += 1
