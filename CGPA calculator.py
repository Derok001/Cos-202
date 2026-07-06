def grade_point(grade):
    grade = grade.upper()

    if grade == "A":
        return 5
    elif grade == "B":
        return 4
    elif grade == "C":
        return 3
    elif grade == "D":
        return 2
    elif grade == "E":
        return 1
    elif grade == "F":
        return 0
    else:
        return -1


print("=" * 40)
print("PERSONAL POCKET CGPA CALCULATOR")
print("=" * 40)

courses = int(input("Enter the number of courses: "))

total_points = 0
total_units = 0

for i in range(courses):
    print(f"\nCourse {i + 1}")

    unit = int(input("Course Unit: "))
    grade = input("Grade (A, B, C, D, E, F): ")

    point = grade_point(grade)

    while point == -1:
        print("Invalid grade! Enter A, B, C, D, E or F.")
        grade = input("Grade: ")
        point = grade_point(grade)

    total_points += point * unit
    total_units += unit

cgpa = total_points / total_units

print("\n========== RESULT ==========")
print(f"Total Units: {total_units}")
print(f"Total Grade Points: {total_points}")
print(f"CGPA: {cgpa:.2f}")

if cgpa >= 4.50:
    print("Class of Degree: First Class")
elif cgpa >= 3.50:
    print("Class of Degree: Second Class Upper")
elif cgpa >= 2.40:
    print("Class of Degree: Second Class Lower")
elif cgpa >= 1.50:
    print("Class of Degree: Third Class")
elif cgpa >= 1.00:
    print("Class of Degree: Pass")
else:
    print("Class of Degree: Fail")