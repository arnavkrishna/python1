people = [
    {"name": "Harry", "house": "gryffindor"},
    {"name": "Cho", "house": "ravenclaw"},
    {"name": "Draco", "house": "slytherin"}
]

#the lambda is like a mini function that says, in this case, take the person and return their name. 

people.sort(key=lambda person: person["name"])

print(people)



