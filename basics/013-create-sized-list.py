
list = [0] * 10 # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list =[[8]* 5] * 10
# [[8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8]]
# CAUTION: [8, 8, 8, 8, 8] in the 2 dimension list are the same object!

list = []
j = 10
for i in range(8):
    list.append( [0] * 10)
print(list) # will be correct one