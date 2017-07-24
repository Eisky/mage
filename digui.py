def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)


a = fact(6)
print(a)


def f(x):
    x = x - 1
print(type(f(9)))