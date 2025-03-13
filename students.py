# students.py

# List of students with dictionaries
students = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "index_number": "123456",
        "nationality": "Polish",
        "starting_date": "2025-03-13",
        "courses": ["Mathematics", "Computer Science", "Physics"]
    },
    {
        "first_name": "Alice",
        "last_name": "Smith",
        "index_number": "654321",
        "nationality": "American",
        "starting_date": "2024-09-01",
        "courses": ["Biology", "Chemistry", "Physics"]
    },
    {
        "first_name": "Carlos",
        "last_name": "Garcia",
        "index_number": "789123",
        "nationality": "Spanish",
        "starting_date": "2023-08-20",
        "courses": ["Engineering", "Mathematics", "Computer Science"]
    }
]

# Display each student's name and index number
for student in students:
    print(f"Name: {student['first_name']} {student['last_name']}, Index: {student['index_number']}")
