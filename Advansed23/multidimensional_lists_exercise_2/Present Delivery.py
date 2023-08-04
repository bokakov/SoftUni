presents = [int(input())]
rows = int(input())
matrix = [[x for x in input().split()] for x in range(rows)]
cols, good_kids_total = len(matrix[0]), [[sum([matrix[row].count("V") for row in range(rows)])] * 2]
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}


def check_valid_idx(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        return True


def find_position():
    for row in range(rows):
        if "S" in matrix[row]:
            col = matrix[row].index("S")
            matrix[row][col] = "-"
            return row, col


def check_steps(row, col, cookie=False):
    if matrix[row][col] == "V":
        good_kids_total[0][0] -= 1
        presents[0] -= 1
    elif cookie and matrix[row][col] == "X":
        presents[0] -= 1
    elif matrix[row][col] == "C":
        cookies(row, col)
    matrix[row][col] = "-"


def cookies(row, col):
    for added_row, added_col in directions.values():
        moving_row, moving_col = row + added_row, col + added_col
        if check_valid_idx(moving_row, moving_col):
            check_steps(moving_row, moving_col, True)


def santa_moving(row, col, direction):
    santa_moving_row, santa_moving_col = row + directions[direction][0], col + directions[direction][1]
    if check_valid_idx(santa_moving_row, santa_moving_col):
        check_steps(santa_moving_row, santa_moving_col)
    return santa_moving_row, santa_moving_col


def check_for_end():
    if good_kids_total[0][0] == 0:
        result(santa_row, santa_col)
        print(f"Good job, Santa! {good_kids_total[0][1]} happy nice kid/s.")
        exit()
    if presents[0] == 0 and good_kids_total[0][0] > 0:
        print("Santa ran out of presents!")
        result(santa_row, santa_col)
        print(f"No presents for {good_kids_total[0][0]} nice kid/s.")
        exit()
    if presents[0] == 0:
        result(santa_row, santa_col)
        print(f"No presents for {good_kids_total[0][0]} nice kid/s.")
        exit()


def result(row, col):
    matrix[row][col] = "S"
    [print(*matrix[row]) for row in range(rows)]


santa_row, santa_col = find_position()
command = input()

while command != "Christmas morning":
    santa_row, santa_col = santa_moving(santa_row, santa_col, command)
    check_for_end()
    command = input()

result(santa_row, santa_col)
print(f"No presents for {good_kids_total[0][0]} nice kid/s.")