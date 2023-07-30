# .sort() works for all primitive value,
# in JS, it only works for string, number will convert to string
# then sort


# to sort without modifying original, use sorted()

list = [1,2,3,4,3,2,9]
list.sort()

sorted_list = sorted(list)
print(sorted_list)

# reverse
sorted_list = sorted(list, reverse=True)
print(sorted_list)

list_obj = [{'age': 3}, {'age': 4}, {'age':1}]
list_obj.sort(key=lambda x: x['age'], reverse=True)
print(list_obj)

