word = input()
for letter in sorted(set(word)):
 print(f"{letter}: {word.count(letter)} time/s")
