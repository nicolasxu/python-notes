
tt = [False, False, True]
res = any(tt)
print (res)


ss = [3,4,8, -1, 0]
res = any(s == 6 for s in ss)
print(res)

res = all(s > 1 for s in ss)
print(res)