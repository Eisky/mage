def sunki(func):
    def demi(x):
        print('Plz enter sth..')
        func(x)
        print('I do not want to tell you')
    return demi

@sunki
def show(x):
    print(x)

print(show('heihei'))