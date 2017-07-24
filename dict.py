d1 = {'x': 32, 'y': [1, 2, 3, 4]}
print(d1['x'])
d1['x'] = 504
print(d1)
print(len(d1))
print(d1.clear())
print(d1.copy())
d2 = d1.copy()
print(d2)
print(id(d1))
# print(help(dict.fromkeys(range(10))))
print(d1.get('x'))
print(d1.items())
print(d1.keys())
print(d1.values())
d2 = {'x': 1, 'y': 2, 'z': 3}
print(d2.popitem())
d1 = {'x': 1, 'y': 2}
d2 = {'m': 21, 'n': 76, 'y': 44}
a = d1.update(d2)
print(a)
i1 = d1.items()
print(i1.next())
