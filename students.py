


students = [
    {
        "first_name": "Akber",
        "last_name": "Elci",
        "index_number": "35397",
        "nationality": "Turkish",
        "starting_date": "3/13/2025",
        "courses": ["Mathematics"]
    },
    {
        "first_name": "Alice",
        "last_name": "Smith",
        "index_number": "654321",
        "nationality": "American",
        "starting_date": "3/13/2025",
        "courses": ["Biology"]
    },
    {
        "first_name": "Carlos",
        "last_name": "Alex",
        "index_number": "789123",
        "nationality": "Spanish",
        "starting_date": "3/13/2025",
        "courses": ["Computer Science"]
    }
]


for student in students:
    print(f"Name: {student['first_name']} {student['last_name']}, Index: {student['index_number']}")
