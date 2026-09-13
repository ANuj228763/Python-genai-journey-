students = []


# Add Student Information Like name , age , markes and other think . 
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = float(input("Enter student marks: "))

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!\n")


# print information about students
def display_students():
    if len(students) == 0:
        print("No students found.\n")
        return

    print("\nStudent List")
    print("------------")

    for student in students:
        print(
            f"Name: {student['name']}, "
            f"Age: {student['age']}, "
            f"Marks: {student['marks']}"
        )

    print()


# find/search student by name and print information about student
def search_student():
    search_name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\nStudent Found")
            print("-------------")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])
            found = True
            break

    if not found:
        print("Student not found.\n")


# Update Student Information
def update_student():
    search_name = input("Enter student name to update: ")

    for student in students:
        if student["name"].lower() == search_name.lower():

            print("\nStudent found.")
            
            new_name = input("Enter new name: ")
            new_age = int(input("Enter new age: "))
            new_marks = float(input("Enter new marks: "))

            student["name"] = new_name
            student["age"] = new_age
            student["marks"] = new_marks

            print("Student updated successfully!\n")
            return

    print("Student not found.\n")

def delete_student():
    search_name = input("Enter student name to delete: ")

    for student in students:
        if student["name"].lower() == search_name.lower():
            students.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")

def highest_marks():
    if len(students) == 0:
        print("No students available.\n")
        return

    highest = students[0]

    for student in students:
        if student["marks"] > highest["marks"]:
            highest = student

    print("\nTop Student")
    print("-----------")
    print("Name:", highest["name"])
    print("Marks:", highest["marks"])
    print()

def average_marks():
    if len(students) == 0:
        print("No students available.\n")
        return

    total = 0

    for student in students:
        total = total + student["marks"]

    average = total / len(students)

    print("Average Marks:", average)
    print()

while True:

    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Find Highest Marks")
    print("7. Find Average Marks")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        highest_marks()

    elif choice == "7":
        average_marks()

    elif choice == "8":
        print("Thank you for using Student Management System.")
        break

    else:
        print("Invalid choice. Please try again.\n")