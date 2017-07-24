import os
import os.path

filename = '/Users/Pisces/Desktop/mao.txt'
if os.path.isfile(filename):
    f1 = open(filename, 'w+')

while True:
    line = input('Enter sth:')
    if line == 'q' or line == 'quit':
        break
    f1.write(line + '\n')

f1.close()
