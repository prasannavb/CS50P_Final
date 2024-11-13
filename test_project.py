# test_project.py
from project import create, read_students, update_students, delete_students, students_details

def test_create():
    students_details.clear()
    student = {
        'rno': 1,
        'name': 'Alice',
        'branch': 'CS',
        'year': 2,
        'marks': {
            'C': 85,
            'python': 90
        }
    }
    result = create(student)
    assert result == "Student record has been created successfully.", "Error: Failed to create student record."
    assert len(students_details) == 1
    assert students_details[0]['name'] == 'Alice'

def test_read_students():
    result = read_students()
    assert result is True, "Read test failed: Expected True for reading existing students."
    assert len(students_details) > 0, "Read test failed: Expected non-empty student list."
    
def test_update_students():
    rno = 1  # Roll number of student to update
    students_details[0]['name'] = "Alice Smith"
    result = update_students(rno)
    assert result =="Student record has been updated successfully."
    assert students_details[0]['name'] == "Alice Smith"

def test_delete_students():
    rno = 1  # Roll number of student to delete
    result = delete_students(rno)
    assert result == "Student record has been deleted successfully.", "Delete test failed: Expected successful deletion."
    assert len(students_details) == 0

