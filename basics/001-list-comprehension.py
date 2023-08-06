fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list3 = [ len(x) for x in fruits]
new_list = [x for x in range(10) if x < 5]
new_list = [ x for x in fruits if "a" in x]
new_list = [ x for x in fruits if x != "apple"]
new_list = [x if 'a' in x and x != "banana" else -1 for x in fruits]
new_list = [x if 'a' in x for x in fruits] # bad one, missing else in the first expression
# new_list2 = [ x for x in fruits if "a" in x else -1] # bad one, else can not be in last if

#  newlist = [expression for item in iterable if condition == True]


print(new_list)