from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'DOB'])

S = Student('Nandini', '19', '2541997')


# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)