students = {
    'Alice': 85,
    'bob': 92,
    'Charlie': 75,
    'Diana': 95,
    'Eve': 88
}

threshold = 90

good_student = {name: grade for name, grade in students.items() if grade >=92}
print(good_student)