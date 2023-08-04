from string import ascii_letters, digits

usernames = input().split(", ")
allowed_chars = ascii_letters + digits + "-" + "_"

for username in usernames:
    if len(username) < 3 or len(username) > 16:
        continue

    has_allowed_char = all([char in allowed_chars for char in username])
    if not has_allowed_char:
        continue

    print(username)
