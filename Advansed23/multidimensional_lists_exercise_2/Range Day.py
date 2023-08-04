SIZE_MATRIX = 5
matrix = [[x for x in input().split()] for _ in range(SIZE_MATRIX)]
target_hits_position, number_of_commands = [], int(input())
total_targets = [sum([matrix[row].count("x") for row in range(SIZE_MATRIX)])]
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}


def check_valid_idx(row, col):
    if 0 <= row < SIZE_MATRIX and 0 <= col < SIZE_MATRIX:
        return True


def find_position():
    for row in range(SIZE_MATRIX):
        if "A" in matrix[row]:
            col = matrix[row].index("A")
            matrix[row][col] = "."
            return row, col


player_row, player_col = find_position()


def shoot(row, col, direction):
    for shooting in range(SIZE_MATRIX):
        shooting_row, shooting_col = row + directions[direction][0], col + directions[direction][1]

        if check_valid_idx(shooting_row, shooting_col):
            if matrix[shooting_row][shooting_col] == "x":
                total_targets[0] -= 1
                target_hits_position.append([shooting_row, shooting_col])
                matrix[shooting_row][shooting_col] = "."
                break

            row, col = shooting_row, shooting_col
        else:
            break


def moving(row, col, direction, steps):
    total_step = [x * steps if x != 0 else 0 for x in directions[direction]]
    moving_row, moving_col = row + total_step[0], col + total_step[1]

    if check_valid_idx(moving_row, moving_col) and matrix[moving_row][moving_col] == ".":
        matrix[row][col] = "."
        matrix[moving_row][moving_col] = "A"
        return moving_row, moving_col
    return row, col


def result():
    [print(x) for x in target_hits_position]


for _ in range(number_of_commands):
    command = input().split()

    if "shoot" in command[0]:
        shoot(player_row, player_col, command[1])
    elif "move" in command[0]:
        player_row, player_col = moving(player_row, player_col, command[1], int(command[-1]))
    if total_targets[0] == 0:
        print(f"Training completed! All {len(target_hits_position)} targets hit.")
        result()
        break

else:
    print(f"Training not completed! {total_targets[0]} targets left.")
    result()