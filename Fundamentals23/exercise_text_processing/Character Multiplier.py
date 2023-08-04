words = input().split()
firs_word = words[0]
second_word = words[1]

min_len = min(len(firs_word), len(second_word))

result = 0

for idx in range(min_len):
    firs_word_char = firs_word[idx]
    second_word_char = second_word[idx]
    result += ord(firs_word_char) * ord(second_word_char)

for idx in range(min_len, len(firs_word)):
    result += ord(firs_word[idx])
for idx in range(min_len, len(second_word)):
    result += ord(second_word[idx])

print(result)
