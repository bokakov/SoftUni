n = int(input())

capacity = 255
tank = 0

for _ in range(n):
    liters = int(input())
    if tank + liters > capacity:
        print(f"Insufficient capacity!")
    else:
        tank += liters
print(tank)
