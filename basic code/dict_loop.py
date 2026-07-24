student = {
    "name": "Sujal",
    "age": 20,
    "course": "Python",
    "course":"python",

}

# for key,values in student.items():
#     print(key)
#     print(values)

# for name in student.keys():
#     print(name.title())

# for name in sorted(student.keys()):
#     print(f"this is sorted {name}")

# for language in student.values():
#     print(language)

for language in set(student.values()):
    print(language)