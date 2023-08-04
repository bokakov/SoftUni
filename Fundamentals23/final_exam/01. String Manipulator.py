string_nc = input()
bool_nc = True

translate_nc = 'Translate'
include_nc = 'Includes'
start_nc = 'Start'
lowercase_nc = 'Lowercase'
find_index_nc = 'FindIndex'
remove_nc = 'Remove'


while bool_nc:

    command_nc = input()

    if command_nc == 'End':
        bool_nc = False
        exit()


    if translate_nc in command_nc:
        ch_nc = str(command_nc[10:11])
        replacement_nc = str(command_nc[12:])

        string_nc = string_nc.replace(ch_nc, replacement_nc)
        print(string_nc)


    if include_nc in command_nc:
        substr_nc = str(command_nc[9:])
        if substr_nc in string_nc:
            print(True)
        else:
            print(False)

    if start_nc in command_nc:
        starting_str_nc = str(command_nc[6:])

        string_list_nc = string_nc.split(" ")

        if starting_str_nc == string_list_nc[0]:
            print(True)
        else:
            print(False)

    if lowercase_nc in command_nc:
        string_nc = string_nc.lower()
        print(string_nc)

    if find_index_nc in command_nc:
        character_nc = command_nc[10:]
        print(string_nc.index(character_nc))

    if remove_nc in command_nc:
        command_list_nc = command_nc.split()
        starting_nc = int(command_list_nc[1])
        ending_nc = int(command_list_nc[2])

        string_nc = len(string_nc).pop[starting_nc:ending_nc]
        print(string_nc)

