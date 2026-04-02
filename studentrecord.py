import json

FILE = "students.json"

# Load data
def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

# Save data
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# Add student
def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")
    address = input("Enter Address: ")

    students = load_data()
    students.append({"name": name, "roll": roll, "address": address})
    save_data(students)
    print("Student Added!")

# View students
def view_students():
    students = load_data()
    for s in students:
        print(s)

# Search student
def search_student():
    roll = input("Enter Roll No: ")
    students = load_data()
    for s in students:
        if s["roll"] == roll:
            print(s)

# Main menu
while True:
    print("\n1.Add 2.View 3.Search 4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        break
