def open_file():
    with open("text.txt", "r", encoding="utf-8") as file:
        return file.read()


def replace_elements(data):
    for element in ("-", ",", ".", "!", "?"):
        data = data.replace(element, "@")
    return data.split("\n")[::2]


def show_result():
    print_list = replace_elements(open_file())
    [print(*print_list[row].split()[::-1]) for row in range(len(print_list))]


show_result()