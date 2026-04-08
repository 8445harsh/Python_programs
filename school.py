# SCHOOL DATA MANAGER 

students = []

# A METHOD FOR ADD A STUDENT
def addStudent():
    roll = input("\n\tEnter Roll Number: ")
    name = input("\tEnter Name: ")
    age = input("\tEnter Age: ")
    grade = input("\tEnter Grade: ")
    gender = input("\tEnter Gender:")
    

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "grade": grade,
        "gender":gender
    }

    students.append(student)
    print("\n\tStudent added successfully!\n")


# A METHOD FOR VIEW STUDENTS
def viewStudents():
    if not students:
        print("\n\tNo records found.\n")
        return

    print("\n\t--- Student Records ---")
    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']},Gender: {s['gender']}")
    print()


#A METHOD FOR SEARCH A STUDENT
def searchStudent():
    roll = input("Enter Roll Number to search: ")
    for s in students:
        if s['roll'] == roll:
            print(f"\n\tFound: {s}")
            return
    print("\n\tStudent not found.\n")


#A METHOD FOR DELETE A STUDENT
def deleteStudent():
    roll = input("\n\tEnter Roll Number to delete: ")
    for s in students:
        if s['roll'] == roll:
            students.remove(s)
            print("\n\tStudent deleted successfully!\n")
            return
    print("\n\tStudent not found.\n")


def menu():
    while True:
        print("\n\t====== School Data Manager ======")
        print("\t1. Add Student")
        print("\t2. View Students")
        print("\t3. Search Student")
        print("\t4. Delete Student")
        print("\t5. Exit")

        ch = input("\n\tEnter your choice: ")

        if ch == "1":
            addStudent()
        elif ch == "2":
            viewStudents()
        elif ch == "3":
            searchStudent()
        elif ch == "4":
            deleteStudent()
        elif ch == "5":
            print("\n\tBYE-BYE ADMIN!")
            break
        else:
            print("\n\tInvalid choice, try again.\n")

# Run Program
menu()
