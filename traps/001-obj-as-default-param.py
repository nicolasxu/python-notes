

def func1(a="", b={}):
    b[a] = 10
    return b

first_b =func1(3)
last_b = func1(4)
# Both function call using the same object
print(f'first_b: {first_b}, last_b: {last_b}')

# first_b: {3: 10, 4: 10}, last_b: {3: 10, 4: 10}


