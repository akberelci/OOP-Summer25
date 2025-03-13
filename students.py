


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



def add_student(first_name, last_name, index_number, nationalty, starting_date, courses):
    students.append({"first_name": first_name, "last_name": last_name, "index_number": index_number, "nationalty": nationalty, "startin_date": starting_date, "courses": courses})


def display_students():
    for student in students:
        print(student["first_name"], student["last_name"], "-", student["index_number"])


display_students()
print("\nAdding a new student...\n")
add_student("alex", "maxi", "112233")
display_students()
