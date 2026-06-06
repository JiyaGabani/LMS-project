# Student Data Organizer
students = []

def add_student():
    print("\n===Enter student details===:")

    student_id = input("Student ID: ")
    name = input("Name: ")
    age = input("Age: ")
    grade = input("Grade: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    subjects = input("Subjects (comma-separated): ").split(",")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "grade": grade,
        "dob": dob,
        "subjects": [s.strip() for s in subjects]
    }

    students.append(student)

    print("\n==Student added successfully!==")


def display_students():
    print("\n======= Display All Students =======")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print(
            f"Student ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Grade: {student['grade']} | "
            f"Subjects: {', '.join(student['subjects'])}"
        )


def update_student():
    student_id = input("\n==Enter Student ID to update==: ")

    for student in students:
        if student["id"] == student_id:
            print("Enter new details:")

            student["name"] = input("New Name: ")
            student["age"] = input("New Age: ")
            student["grade"] = input("New Grade: ")
            student["dob"] = input("New Date of Birth (YYYY-MM-DD): ")

            subjects = input("New Subjects (comma-separated): ")
            student["subjects"] = [s.strip() for s in subjects.split(",")]

            print("Student information updated successfully!")
            return

    print("Student not found!")


def delete_student():
    student_id = input("\n==Enter Student ID to delete==: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found!")

def display_subjects():
    print("\n===== Subjects Offered =====")

    all_subjects = set()

    for student in students:
        for subject in student["subjects"]:
            all_subjects.add(subject)

    if all_subjects:
        for subject in all_subjects:
            print(subject)
    else:
        print("No subjects available.")


# Main Menu
while True:
    print("\nWelcome to the Student Data Organizer!")
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")
if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        display_subjects()

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")

