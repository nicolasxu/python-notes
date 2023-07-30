# https://www.w3schools.com/python/ref_func_slice.asp
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2) # 2 is end index, not inclusive
print(a[x]) # ('a', 'b')

# slice(start, end, step)
# start 	Optional. An integer number specifying at which position to start the slicing. Default is 0
# end 	An integer number specifying at which position to end the slicing
# step 	Optional. An integer number specifying the step of the slicing. Default is 1

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])


################################################################

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x]) #('a', 'd', 'g')