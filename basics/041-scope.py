x = 1
def func():
    # print(x) # this will result an error, since you access x in func scope before it is defined
      # this is compile time. Python proof reading the code and foud an error: var is used before it is defined
    x = 2
    # in python you have to define a var before using
func()

# https://www.youtube.com/watch?v=38uGbVYICwg



############################################################################
t = 1
def outer():
    t = 2
    def inner():
        nonlocal t
        # global t
        t = 3
        print(f'inner t val: {t}')
    inner()
    print(f'outer t val: {t}')

outer()
print(f'global t val: {t}')



