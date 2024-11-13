# Student Management System

This project is a Python-based console application to manage student records. It provides options to create, read, update, and delete student information, including details like registration number, name, branch, year, and marks for specific subjects.

## DEMO
[Demo Video](https://youtu.be/k5BMcKGIhew)

## Features

- **Add New Student Record**: Allows users to add a new student with details such as registration number, name, branch, year of study, and marks in C and Python.
- **View All Student Records**: Displays all stored student records in a list format.
- **Update Existing Student Record**: Updates a student's details based on their registration number.
- **Delete Student Record**: Deletes a student record by registration number.

## Prerequisites

- Python 3.10 or higher (for the `match` statement compatibility)

## How to Use

1. Clone this repository or copy the code to your local Python environment.
2. Run the program by executing the following command:

    ```bash
    python <filename>.py
    ```

3. The main menu offers the following options:

    - **1. Create a new student record**: Prompts for the student's details and saves them in the record.
    - **2. View all student records**: Displays a list of all saved student records.
    - **3. Update an existing student record**: Prompts for a registration number and allows updating specific details.
    - **4. Delete a student record**: Deletes a student's record based on the registration number.

4. After each action, the program will prompt if you want to continue. Enter 'Y' to go back to the main menu or 'N' to exit.

## Code Structure

- `students_details`: A list that holds student dictionaries. Each dictionary represents a student.
- `get_student_details()`: Function that prompts for and collects student details.
- `create(student)`: Adds a new student record to `students_details`.
- `read_students()`: Displays all student records in `students_details`.
- `update_students(rno)`: Updates an existing student record based on the provided registration number.
- `delete_students(rno)`: Deletes a student record by registration number.
- `main()`: The main function that handles the menu and user input.

## Sample Workflow

1. **Create a Record**:
   - Enter the student’s registration number, name, branch, year, and marks in C and Python.
   - Confirmation message: *"Student record has been created successfully."*

2. **View Records**:
   - Displays each student’s registration number, name, branch, year, and marks.

3. **Update a Record**:
   - Enter the registration number of the student to update.
   - Choose to keep existing data or enter new values for each field.
   - Confirmation message: *"Student record has been updated successfully."*

4. **Delete a Record**:
   - Enter the registration number of the student to delete.
   - Confirmation message: *"Student record has been deleted successfully."*

## Example Usage

```
Choose an option:
1. Create a new student record
2. View all student records
3. Update an existing student record
4. Delete a student record
Enter your choice (1-4): 1

Enter the student’s registration number: 101
Enter the student’s name: John Doe
Enter the student’s branch: Computer Science
Enter the student’s year of study: 2
Enter the marks for C programming: 85
Enter the marks for Python programming: 90

Student record has been created successfully.
```

## Error Handling

- If no students are available to display in `read_students()`, it will print: *"No student records available to display."*
- If a student record with the specified registration number is not found in `update_students()` or `delete_students()`, it will return an error message.

## Requirements

- Python 3.10 or higher


Made with efforts by Prasanna V B .Enjoy using the app!!
---

