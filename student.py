# -*- coding: utf-8 -*-
"""Student.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X_to5fVpSdj3t-08THMjuybUHaaodK05
"""

students_details = []

def get_student_details():
    student = {
        'rno': '',
        'name': '',
        'branch': '',
        'year': '',
        'marks': {
            'C': '',
            'python': ''
        }
    }
    student['rno'] = int(input('Enter the student’s registration number: '))
    student['name'] = input('Enter the student’s name: ')
    student['branch'] = input('Enter the student’s branch: ')
    student['year'] = int(input('Enter the student’s year of study: '))
    student['marks']['C'] = int(input('Enter the marks for C programming: '))
    student['marks']['python'] = int(input('Enter the marks for Python programming: '))
    return student

def create(student):
    if student:
        students_details.append(student)
        return "Student record has been created successfully."
    else:
        return "Error: Failed to create student record."

def read_students():
    if not students_details:
        print("No student records available to display.")
        return False
    else:
        print("\nList of Students:")
        for student in students_details:
            print(f"Registration Number: {student['rno']}, Name: {student['name']}, Branch: {student['branch']}, Year: {student['year']}, C Marks: {student['marks']['C']}, Python Marks: {student['marks']['python']}")
        return True

def update_students(rno):
    student_to_update = None
    for student in students_details:
        if student['rno'] == rno:
            student_to_update = student
            break

    if student_to_update:
        new_name = input(f"Enter new name (or press Enter to keep '{student_to_update['name']}'): ")
        new_branch = input(f"Enter new branch (or press Enter to keep '{student_to_update['branch']}'): ")
        new_year = input(f"Enter new year of study (or press Enter to keep '{student_to_update['year']}'): ")
        new_c_mark = input(f"Enter new C marks (or press Enter to keep '{student_to_update['marks']['C']}'): ")
        new_python_mark = input(f"Enter new Python marks (or press Enter to keep '{student_to_update['marks']['python']}'): ")

        student_to_update['name'] = new_name if new_name else student_to_update['name']
        student_to_update['branch'] = new_branch if new_branch else student_to_update['branch']
        student_to_update['year'] = int(new_year) if new_year else student_to_update['year']
        student_to_update['marks']['C'] = int(new_c_mark) if new_c_mark else student_to_update['marks']['C']
        student_to_update['marks']['python'] = int(new_python_mark) if new_python_mark else student_to_update['marks']['python']
        return "Student record has been updated successfully."
    else:
        return "Error: Student with the given registration number was not found."

def delete_students(rno):
    index = -1
    for i, student in enumerate(students_details):
        if student['rno'] == rno:
            index = i
            break

    if index != -1:
        students_details.pop(index)
        return "Student record has been deleted successfully."
    else:
        return "Error: Student with the given registration number was not found."

def main():
    while True:
        print("\nStudent Database Management System")
        print("Choose an option:")
        print("1. Create a new student record")
        print("2. View all student records")
        print("3. Update an existing student record")
        print("4. Delete a student record")
        ch = int(input("Enter your choice (1-4): "))

        match ch:
            case 1:
                student = get_student_details()
                print(create(student))
            case 2:
                read_students()
            case 3:
                rno = int(input("Enter the student’s registration number to update: "))
                print(update_students(rno))
            case 4:
                rno = int(input("Enter the student’s registration number to delete: "))
                print(delete_students(rno))
            case _:
                print("Invalid choice. Please select a valid option.")

        choice = input("Do you want to continue? (Y/N): ").upper().strip()
        if choice == 'N':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()