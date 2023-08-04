from collections import deque

bees = deque(int(x) for x in input().split())
nectars = deque(int(x) for x in input().split())
operations = deque(input().split())

total_honey = 0

operators = {
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
}

while bees and nectars:
    curr_bee = bees.popleft()
    curr_nectar = nectars.pop()

    if curr_nectar < curr_bee:
        bees.appendleft(curr_bee)
    elif curr_nectar > curr_bee:
        total_honey += abs(operators[operations.popleft()](curr_bee, curr_nectar))
print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectars:
    print(f"Nectar left: {', '.join(str(x) for x in nectars)}")