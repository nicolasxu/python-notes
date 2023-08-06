dict1= {'a': 10}
dict2={'b': 11}

d3 = dict1 | dict2 # '+' is not supported
print(d3)

d3 = {**dict1, **dict2}
print(d3)