numbers = input().split(", ")


def check_palindrome(nums):
    for n in nums:
        if n == n[::-1]:
            print("True")
        else:
            print("False")


check_palindrome(numbers)
