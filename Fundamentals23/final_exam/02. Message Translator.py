import re

input_nc = int(input())
pattern_nc = r'!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})]'

for _ in range(input_nc):
    msg_to_translate_nc = input()
    matches_nc = re.findall(pattern_nc, msg_to_translate_nc)
    final_translation_nc = []

    if matches_nc:
        data_nc = matches_nc[0]
        message_nc = data_nc[1]
        for i in message_nc:
            final_translation_nc.append(str(ord(i)))
        print(f"{data_nc[0]}: {' '.join(final_translation_nc)}")

    else:
        print("The message is invalid")
