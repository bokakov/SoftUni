input_word = input().split(' ')
result = []

for word in input_word:
    char_as_ascii = [char for char in word if char.isdigit()]
    word_as_str = [char for char in word if char.isalpha()]

    first_letter = chr(int(''.join(char_as_ascii)))
    word_as_str[0], word_as_str[-1] = word_as_str[-1], word_as_str[0]
    new_word = first_letter + ''.join(word_as_str)
    result.append(new_word)

print(' '.join(result))
