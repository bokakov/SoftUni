from collections import deque

food = int(input())
clients = deque([int(x) for x in input().split()])

print(max(clients))

for client in clients.copy():
    if food >= client:
        clients.popleft()
        food -= client
    else:
        print(f"Orders left: {' '.join([str(x) for x in clients])}")
        break
else:
    print("Orders complete")
