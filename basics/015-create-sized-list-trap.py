m = 5
n = 3

list = [[0]*m]*n # bug: each row is the same obejct reference
list[0][0] =1  # will set values in first column to 1
print(list)
# [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
list = [[0 for m in range(m)] for n  in range(n)]
list[1][1] = 333
print(list)