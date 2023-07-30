

# Python is function scope, not block scope
# Syntax: nonlocal can only be used as declaration, not assignment
#         nonlocal x = 10 will be an syntax error

def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())  # hello

# if you remove nonlocal x, then the result is "John"



