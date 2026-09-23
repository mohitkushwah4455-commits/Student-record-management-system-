students = []

# Module 1: Add Student
def add_student():
    print("\n--- Add Student ---")

    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    branch = input("Enter Branch: ")
    marks = float(input("Enter Marks: "))

    student = {
        "roll": roll,
        "name": name,
        "branch": branch,
        "marks": marks
    }

    students.append(student)
    print("Student record added successfully!")


# Module 2: Search Student
def search_student():
    print("\n--- Search Student ---")

    roll = input("Enter Roll Number: ")

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found")
            print("Roll Number:", student["roll"])
            print("Name:", student["name"])
            print("Branch:", student["branch"])
            print("Marks:", student["marks"])
            return

    print("Student not found!")


# Module 3: Update Marks
def update_marks():
    print("\n--- Update Marks ---")

    roll = input("Enter Roll Number: ")

    for student in students:
        if student["roll"] == roll:
            new_marks = float(input("Enter New Marks: "))
            student["marks"] = new_marks

            print("Marks updated successfully!")
            return

    print("Student not found!")


# Module 4: Display All Students
def display_students():
    print("\n--- All Student Records ---")

    if len(students) == 0:
        print("No student records available.")
        return

    for student in students:
        print("-------------------------")
        print("Roll Number:", student["roll"])
        print("Name:", student["name"])
        print("Branch:", student["branch"])
        print("Marks:", student["marks"])


# Main Menu
while True:
    print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Marks")
    print("4. Display All Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        search_student()

    elif choice == "3":
        update_marks()

    elif choice == "4":
        display_students()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid, try again.")
