
list1 = [1,2,3]
list2 = [4,5,6]

list3 = list1 + list2
print(list3)

ll = list1.extend(list2)
# ll is None, since extend return None
print (ll)
print(list1) # list1 is changed in place