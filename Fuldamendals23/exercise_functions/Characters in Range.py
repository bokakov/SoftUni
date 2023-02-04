def get_chars(start, end):
    result = ''
    for num in range(ord(start) + 1, ord(end)):
        result += f'{chr(num)} '

    return result


start_char = input()
end_char = input()

print(get_chars(start_char, end_char))
