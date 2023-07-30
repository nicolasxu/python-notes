
# method 1
list = [1,2,'hello', 'world']
list.insert(2, 'good')
print(list)


# method 2
list = [1,2,3, 4]
list[2:2] = ['good', 'bye'] # can only be iterable here
list[1:1] = 'good' # will add each letter a item of list, since 'good' is iterable
print(list)

#  https://www.youtube.com/shorts/OHlbq-N6X2o