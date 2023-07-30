# decorator useMemo:
#  https://www.youtube.com/shorts/-9m7VeZcxVk
from functools import lru_cache

@lru_cache
def increment(num):
    print('running 100 lines')
    return num + 1


print(increment(1))
print(increment(2))
print(increment(3))
print(increment(4))
print(increment(1))


