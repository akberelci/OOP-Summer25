# student_details_structure.py

# Creating a dictionary to store student details
student = {
    "first_name": "John",
    "last_name": "Doe",
    "index_number": "123456",
    "nationality": "Polish",
    "starting_date": "2025-03-13",
    "courses": ["Mathematics", "Computer Science", "Physics"]
}

# Displaying student details
print(f"Name: {student['first_name']} {student['last_name']}")
print(f"Index Number: {student['index_number']}")
print(f"Nationality: {student['nationality']}")
print(f"Starting Date: {student['starting_date']}")
print(f"Courses: {', '.join(student['courses'])}")
