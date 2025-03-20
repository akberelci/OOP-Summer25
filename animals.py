animals = [
    {"name": "Dog", "group": "Mammals", "number_of_legs": 4, "skills": ["Running", "Barking"]},
    {"name": "Bird", "group": "Birds", "number_of_legs": 2, "skills": ["Flying"]},
    {"name": "Cat", "group": "Mammals", "number_of_legs": 4, "skills": ["Jumping", "Climbing"]},
    {"name": "Cow", "group": "Mammals", "number_of_legs": 4, "skills": ["Grazing", "Producing milk"]},
    {"name": "Snake", "group": "Reptiles", "number_of_legs": 0, "skills": ["Slithering", "Hunting"]}
]

print(animals)

class Animal:
    def __init__(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills

animals = [
    Animal("Dog", "Mammals", 4, ["Running", "Barking"]),
    Animal("Bird", "Birds", 2, ["Flying"]),
    Animal("Cat", "Mammals", 4, ["Jumping", "Climbing"]),
    Animal("Cow", "Mammals", 4, ["Grazing", "Producing milk"]),
    Animal("Snake", "Reptiles", 0, ["Slithering", "Hunting"]),
]

for animal in animals:
    print(animal.name, animal.group, animal.number_of_legs, animal.skills)
