# Student Marks Manager
# Created by Dipendu Dey 

import os

FILENAME = "students.txt"

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    python_marks = int(input("Enter Python Marks: "))
    math_marks = int(input("Enter Math Marks: "))
    dbms_marks = int(input("Enter DBMS Marks: "))
    total = python_marks + math_marks + dbms_marks
    average = total / 3

    with open(FILENAME, "a") as f:
        f.write(f"{roll},{name},{python_marks},{math_marks},{dbms_marks},{total},{average:.2f}\n")
    print(" Student record added successfully.\n")

def display_all():
    if not os.path.exists(FILENAME):
        print(" No records found.\n")
        return
    print("\nAll Student Records:")
    print("-" * 70)
    with open(FILENAME, "r") as f:
        for line in f:
            data = line.strip().split(",")
            print(f"Roll: {data[0]}, Name: {data[1]}, Python: {data[2]}, Math: {data[3]}, DBMS: {data[4]}, Total: {data[5]}, Avg: {data[6]}")
    print()

def search_student():
    roll = input("Enter Roll Number to search: ")
    found = False
    with open(FILENAME, "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == roll:
                print(f"\n Found Student - Roll: {data[0]}, Name: {data[1]}, Python: {data[2]}, Math: {data[3]}, DBMS: {data[4]}, Total: {data[5]}, Avg: {data[6]}\n")
                found = True
                break
    if not found:
        print(" Student not found.\n")

def update_student():
    roll = input("Enter Roll Number to update: ")
    updated = False
    new_lines = []
    with open(FILENAME, "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == roll:
                print(" Updating marks for:", data[1])
                python_marks = int(input("New Python Marks: "))
                math_marks = int(input("New Math Marks: "))
                dbms_marks = int(input("New DBMS Marks: "))
                total = python_marks + math_marks + dbms_marks
                average = total / 3
                new_line = f"{roll},{data[1]},{python_marks},{math_marks},{dbms_marks},{total},{average:.2f}\n"
                new_lines.append(new_line)
                updated = True
            else:
                new_lines.append(line)
    with open(FILENAME, "w") as f:
        f.writelines(new_lines)
    if updated:
        print(" Record updated successfully.\n")
    else:
        print(" Student not found.\n")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    deleted = False
    new_lines = []
    with open(FILENAME, "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] != roll:
                new_lines.append(line)
            else:
                deleted = True
    with open(FILENAME, "w") as f:
        f.writelines(new_lines)
    if deleted:
        print(" Record deleted successfully.\n")
    else:
        print(" Student not found.\n")

def main_menu():
    while True:
        print("\n==== Student Marks Manager ====")
        print("1. Add Student Record")
        print("2. Display All Records")
        print("3. Search by Roll Number")
        print("4. Update Marks")
        print("5. Delete Record")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            display_all()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print(" Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice! Try again.")

if __name__ == "__main__":
    main_menu()
