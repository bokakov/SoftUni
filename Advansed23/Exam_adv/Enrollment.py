def gather_credits(needed_credits, *courses):
    enrolled_courses_nc = set()
    gathered_credits_nc = 0

    for course in courses:
        course_name_nc, course_credits_nc = course

        if course_name_nc in enrolled_courses_nc:
            continue

        gathered_credits_nc += course_credits_nc
        enrolled_courses_nc.add(course_name_nc)

        if gathered_credits_nc >= needed_credits:
            break

    if gathered_credits_nc >= needed_credits:
        sorted_courses = sorted(enrolled_courses_nc)
        return f"Enrollment finished! Maximum credits: {gathered_credits_nc}.\nCourses: {', '.join(sorted_courses)}"
    else:
        credits_shortage = needed_credits - gathered_credits_nc
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."

# print(gather_credits(
#     80,
#     ("Basics", 27),
# ))

# print(gather_credits(
#     80,
#     ("Advanced", 30),
#     ("Basics", 27),
#     ("Fundamentals", 27),
# ))

