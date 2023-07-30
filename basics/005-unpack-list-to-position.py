


list = [1,2,3,4]
# print(*list) # 1 2 3 4

l2 = [*list]
# print(l2) # [1, 2, 3, 4]

str = "1234567890"

l2 = [map(lambda x: x, str)] # [<map object at 0x101ac4d60>]
l2 = [*map(lambda x: x, str)] # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# print(l2)


def my_fn(*args):
    print(args)
my_fn(*list) # (1, 2, 3, 4)