username_license_plate = {}
count = int(input())
for _ in range(count):
    command_arguments = input().split()
    command = command_arguments[0]
    username = command_arguments[1]

    if command == "register":
        license_plate = command_arguments[2]
        if username in username_license_plate:
            print(f"ERROR: already registered with plate number {username_license_plate[username]}")
        else:
            username_license_plate[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    else:
        if username in username_license_plate:
            username_license_plate.pop(username)
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for username, license_plate in username_license_plate.items():
    print(f"{username} => {license_plate}")
