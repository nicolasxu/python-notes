# 1. reverse list
s = [1,2,3,4]
s.reverse()
print(s.reverse()) # // will print nothing, since reverse() return None
print(s)


# 2. reverse string
s = "12345"
reversed_s = s[::-1] # there is no reverse() function for string
print(reversed_s)

s = "12345"
# splited = s.split("") # you can not split with empty space
splited2 = [char for char in s].reverse() # splited2 will be None,
# since reverse() return None
print(splited2)