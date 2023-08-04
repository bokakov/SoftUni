students_by_course = {}

while True:
    command = input()
    if command == "end":
        break
    args = command.split(' : ')
    name_of_course = args[0]
    students_name = args[1]

    if name_of_course not in students_by_course:
        students_by_course[name_of_course] = []

    students_by_course[name_of_course].append(students_name)

for name_of_course, students in students_by_course.items():
    print(f"{name_of_course}: {len(students)}")

    for student in students:
        print(f"-- {student}")
        