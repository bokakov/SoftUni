while True:
    line = input()
    if line == "End":
        break

    if line == "SoftUni":
        continue

    for char in line:
        print(f"{char}{char}", end="")

    print()