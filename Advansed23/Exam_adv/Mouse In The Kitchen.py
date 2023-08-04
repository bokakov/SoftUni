def move_mouse_nc(matrix_nc, directions_nc):
    n = len(matrix_nc)
    m = len(matrix_nc[0])
    mouse_position = None
    cheese_count = 0

    for i in range(n):
        for j in range(m):
            if matrix_nc[i][j] == 'M':
                mouse_position = (i, j)
            
            elif matrix_nc[i][j] == 'C':
                cheese_count += 1

    for direction in directions_nc:
        if direction == "danger":
            print("Mouse will come back later!")
            break

        x, y = mouse_position
        if direction == "up":
            x -= 1
        
        elif direction == "down":
            x += 1
        
        elif direction == "left":
            y -= 1
        
        elif direction == "right":
            y += 1

        if x < 0 or x >= n or y < 0 or y >= m:
            print("No more cheese for tonight!")
            break

        if matrix_nc[x][y] == "*":
            matrix_nc[mouse_position[0]][mouse_position[1]] = "*"
            mouse_position = (x, y)
            matrix_nc[x][y] = "M"
        
        elif matrix_nc[x][y] == "C":
            matrix_nc[mouse_position[0]][mouse_position[1]] = "*"
            mouse_position = (x, y)
            matrix_nc[x][y] = "M"
            cheese_count -= 1
            
            if cheese_count == 0:
                print("Happy mouse! All the cheese is eaten, good night!")
                break
        
        elif matrix_nc[x][y] == "T":
            matrix_nc[mouse_position[0]][mouse_position[1]] = "*"
            mouse_position = (x, y)
            matrix_nc[x][y] = "M"
            print("Mouse is trapped!")
            break

    for row in matrix_nc:
        print(''.join(row))


rows, cols = map(int, input().split(","))
md_list = []
for _ in range(rows):
    md_list.append(list(input()))

directions = []
while True:
    direction = input()
    
    if direction == "danger":
        directions.append(direction)
        break
    directions.append(direction)

move_mouse_nc(md_list, directions)
