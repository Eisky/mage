from multiprocessing import Process
import os
import time

def info(title):
    print(title)
    print('module name:', __name__)
    if hasattr(os, 'getppid'):
        print('Parent process:', os.getppid())

    time.sleep(4)
    print('Process id:', os.getppid())

def f(name):
    info('function f')
    print('hello', name)

if __name__=='__main__':
    info('main line')
    print('________')
    p = Process(target=f, args=['sunki'])
    p.start()
    p.join()