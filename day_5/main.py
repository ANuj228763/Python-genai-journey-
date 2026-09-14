students = []

def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = float(input("Enter student marks: "))

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully! ")
    
def display_students():
    print("\n--- Student List ---")

    if len(students) == 0:
        print("No students found.")
        return

    for index, student in enumerate(students, start=1):
        print(
            f"{index}. "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Marks: {student['marks']}"
        )


def search_student():
    print("\n--- Search Student ---")

    name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent Found ")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])

            found = True
            break

    if not found:
        print("Student not found. ")

def update_student():
    print("\n--- Update Student ---")

    name = input("Enter students name to update: ")

    for student in students:
        if student["name"].lower() == name.lower():

            print("Student found.")
            print("1.Update Name")
            print("2.Update Age")
            print("3. Update Marks")

            choice = input("Enter your choice: ")

            if choice == "1":
                student["name"] = input("Enter new name: ")
                print("Name updated successfully. ")

            elif choice == "2":
                student["age"] = int(input("Enter new age: "))
                print("Age updated successfully. ")

            elif choice == "3":
                student["marks"] = float(input("Enter new marks: "))
                print("Marks updated successfully. ")

            else:
                print("Invalid choice. ")

            return

    print("Student not found. ")

def delete_student():
    print("\n--- Delete Student ---")

    name = input("Enter student name to delete: ")

    for student in students:
        if student["name"].lower() == name.lower():

            students.remove(student)

            print("Student deleted successfully. ")
            return

    print("Student not found. ")


def calculate_average():
    print("\n--- Average Marks ---")

    if len(students) == 0:
        print("No students available.")
        return

    total_marks = 0

    for student in students:
        total_marks += student["marks"]

    average = total_marks / len(students)

    print(f"Average Marks: {average:.2f}")


def find_top_student():
    print("\n--- Top Student ---")

    if len(students) == 0:
        print("No students available.")
        return

    top_student = students[0]

    for student in students:
        if student["marks"] > top_student["marks"]:
            top_student = student

    print("Top Student ")
    print("Name:", top_student["name"])
    print("Age:", top_student["age"])
    print("Marks:", top_student["marks"])


def main():
    while True:

        print("\n====== STUDENT MANAGEMENT ======")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Average Marks")
        print("7. Top Student")
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
            calculate_average()

        elif choice == "7":
            find_top_student()

        elif choice == "8":
            print("Thank you for using Student Management System! ")
            break

        else:
            print("Invalid choice. Please try again. ")
            
main()