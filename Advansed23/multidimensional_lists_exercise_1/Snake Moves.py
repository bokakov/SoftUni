rows, cols = [int(x) for x in input().split()]
text = input()

index_snake = 0

for row in range(rows):
    result = []
    for col in range(cols):
        if index_snake == len(text):
            index_snake = 0
        if row % 2 == 0:
            result.append(text[index_snake])
        else:
            result.insert(0, text[index_snake])

        index_snake += 1

    print(*result, sep="")