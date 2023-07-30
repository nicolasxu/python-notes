

# reduce(func_name, iterable, initializer)

from functools import reduce
start = 30
nums = [x for x in range(10)]


print(reduce(lambda x, y: x + y, nums, start))