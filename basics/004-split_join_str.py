
# method 1, split with empty string
str = '11111'
l = list(str) # ['1', '1', '1', '1', '1']
print(l)

# method 2, split with lambda
l = [*map(lambda x: x, str)] # ['1', '1', '1', '1', '1']
print(l)

# method 3, split with delimiter
str = "hello work nick!"
l = str.split(" ") # you can not provide "" as empty string
print(l) # ['hello', 'work', 'nick!']


# join list to string
delimiter = ", "
list = ["hello", "workd", "nick!"]
str = delimiter.join(list) # hello, workd, nick!
print(str)