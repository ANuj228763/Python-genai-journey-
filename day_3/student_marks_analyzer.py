

marks = [56, 92, 41, 59, 82, 73]


total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)


passed = 0
failed = 0

for mark in marks:
    if mark >= 40:
        passed += 1
    else:
        failed += 1

print("Student Marks Analyzer")
print("-----------------------")
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed Subjects:", passed)
print("Failed Subjects:", failed)


print("\nGrades:")

for mark in marks:
    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 40:
        grade = "D"
    else:
        grade = "F"

    print(mark, "→", grade)