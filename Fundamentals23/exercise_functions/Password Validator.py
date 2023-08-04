def validate(password):
    count = 0
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        print("Password must consist only of letters and digits")
    for char in password:
        if char.isdigit():
            count += 1
    if count < 2:
        print("Password must have at least 2 digits")
    if 6 <= len(password) <= 10 and password.isalnum() and count >= 2:
        print("Password is valid")


current_password = input()
validate(current_password)










































# def validate_password(password):
#     errors = []
#     if not valid_length(password):
#         errors.append("Password must be between 6 and 10 characters")
#
#     if not contains_alpha_num_chars(password):
#         errors.append("Password must consist only of letters and digits")
#
#     if not contains_two_digits(password):
#         errors.append("Password must have at least 2 digits")
#
#         return errors
#
#
# def valid_length(password):
#     return 6 <= len(password) <= 10
#
#
# def contains_alpha_num_chars(password):
#     return password.isalnum()
#
#
# def contains_two_digits(password):
#     digits_count = 0
#     for char in password:
#         if char.isdigit():
#             digits_count += 1
#
#     return digits_count >= 2
#
#
# input_password = input()
# errors = validate_password(input_password)
#
# if len(errors):
#     for error in errors:
#         print(error)
# else:
#     print("Password is valid")
