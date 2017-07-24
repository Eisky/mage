url = 'www.magedu.com';x = 0

while url:
    print(url)
    url = url[:-1]
    x+=1
    if x > 7:
        break
else:
    print('over')
a = 0; b = 100; list=[]
while a < b:
    a+=2
    print(a)
c = list.append(a)
print(c)
di = {'x':1,'y':23,'z':78}
for a in di.keys():
    print(a)
print(sum(n for n in range(101)))
l = ['a','b','c','d']
for x in range(1,len(l),2):
    print(l[x])