n = int(input())

student_grades = {}
for _ in range(n):
    student_name = input()
    student_grade = float(input())

    if student_name not in student_grades:
        student_grades[student_name] = []

    student_grades[student_name].append(student_grade)

for student, grades in student_grades.items():
    avg_grade = sum(grades) / len(grades)
    if avg_grade < 4.50:
        continue
    print(f"{student} -> {avg_grade:.2f}")
