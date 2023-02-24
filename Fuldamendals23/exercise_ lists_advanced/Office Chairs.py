rooms = int(input())

free_chairs = 0
game_on = True

for room in range(1, rooms + 1):
    chairs, guests_str = input().split()
    guest = int(guests_str)

    if guest > len(chairs):
        needed_chairs = guest - len(chairs)
        print(f"{needed_chairs} more chairs needed in room {room}")
        game_on = False

    else:
        free_chairs_row = len(chairs) - guest
        free_chairs += free_chairs_row


if game_on:
    print(f"Game On, {free_chairs} free chairs left")
