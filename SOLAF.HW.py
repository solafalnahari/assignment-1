students = {}

def add_student():
    student_id = input("Enter Student ID: ").strip()

    if student_id in students:
        print("Error: Student ID already exists!")
        return

    name = input("Enter Student Name: ").strip()

    while True:
        try:
            grade = float(input("Enter Student Grade (0-100): "))
            if 0 <= grade <= 100:
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    students[student_id] = {
        "name": name,
        "grade": grade
    }

    print("Student added successfully.")


def show_all_students():
    if not students:
        print("No students found.")
        return

    print("\n----- Student List -----")
    for student_id, info in students.items():
        print(f"ID: {student_id}")
        print(f"Name: {info['name']}")
        print(f"Grade: {info['grade']}")
        print("-" * 25)


def search_student():
    student_id = input("Enter Student ID to search: ").strip()

    if student_id in students:
        info = students[student_id]
        print(f"\nID: {student_id}")
        print(f"Name: {info['name']}")
        print(f"Grade: {info['grade']}")
    else:
        print("Student not found.")


def update_grade():
    student_id = input("Enter Student ID: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    while True:
        try:
            new_grade = float(input("Enter new grade: "))
            if 0 <= new_grade <= 100:
                students[student_id]["grade"] = new_grade
                print("Grade updated successfully.")
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def delete_student():
    student_id = input("Enter Student ID: ").strip()

    if student_id in students:
        del students[student_id]
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def calculate_average():
    if not students:
        print("No students available.")
        return

    total = 0

    for info in students.values():
        total += info["grade"]

    average = total / len(students)
    print(f"Average Grade: {average:.2f}")


def show_best_student():
    if not students:
        print("No students available.")
        return

    best_id = max(students, key=lambda x: students[x]["grade"])
    info = students[best_id]

    print("\nBest Student")
    print(f"ID: {best_id}")
    print(f"Name: {info['name']}")
    print(f"Grade: {info['grade']}")


def show_worst_student():
    if not students:
        print("No students available.")
        return

    worst_id = min(students, key=lambda x: students[x]["grade"])
    info = students[worst_id]

    print("\nWorst Student")
    print(f"ID: {worst_id}")
    print(f"Name: {info['name']}")
    print(f"Grade: {info['grade']}")


def total_students():
    print(f"Total Number of Students: {len(students)}")


def show_passed_students():
    if not students:
        print("No students available.")
        return

    found = False

    print("\nPassed Students:")
    for student_id, info in students.items():
        if info["grade"] >= 60:
            print(f"ID: {student_id}, Name: {info['name']}, Grade: {info['grade']}")
            found = True

    if not found:
        print("No passed students.")


def show_failed_students():
    if not students:
        print("No students available.")
        return

    found = False

    print("\nFailed Students:")
    for student_id, info in students.items():
        if info["grade"] < 60:
            print(f"ID: {student_id}, Name: {info['name']}, Grade: {info['grade']}")
            found = True

    if not found:
        print("No failed students.")


def menu():
    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student by ID")
    print("4. Update Student Grade")
    print("5. Delete Student")
    print("6. Calculate Average Grade")
    print("7. Show Best Student")
    print("8. Show Worst Student")
    print("9. Show Total Number of Students")
    print("10. Show Passed Students")
    print("11. Show Failed Students")
    print("12. Exit")



while True:
    menu()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice! Please enter a number from 1 to 12.")
        continue

    if choice == 1:
        add_student()
