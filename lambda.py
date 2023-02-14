people = [
    {"name": "Harry", "house": "Carpuela"},
    {"name": "Cho", "house": "Ambato"},
    {"name": "Chei", "house": "Quito"}
]

print(people)

def f(person):
    return person["name"]

people.sort(key=f)

print(people)

def f(person):
    return person["house"]

people.sort(key=f)
print(people)

people.sort(key=lambda person: person["name"])
print(people)
