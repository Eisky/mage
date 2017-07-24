from functools import reduce
l1 = [1,2,3,4]
l2 = ['MON','TUE','WED','THU']
a = map(None,l1,l2)
print(a.__next__)
def f4(x,y):
    return x*2,y*2
print(map(f4,l1,l2))
def f5(x,y):
    return x+y
print(reduce(f5,l1,3))
print(type(a))

