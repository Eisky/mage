def getNum(x):
    n = 1
    while n <= x:
        yield n ** 2
        n += 1


g1 = getNum(15)
for i in g1:
    print(i)