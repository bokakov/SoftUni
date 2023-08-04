text = input()
encrypted_text = ""
for char in text:
    ascii_value = ord(char) + 3
    encrypted_text += chr(ascii_value)

print(encrypted_text)
