num_dict = {}
line = input()

while line != "Search":

    num_as_str = line
    try:
        number = int(input())
        num_dict[num_as_str] = number
    except ValueError:
        print("The variable number must be an integer")
    line = input()

line = input()

while line != "Remove":
    searched = line
    try:
        print(num_dict[searched])
    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

line = input()
while line != "End":
    searched = line
    try:
        del num_dict[searched]
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

print(num_dict)