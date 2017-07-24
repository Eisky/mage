from multiprocessing import Pool

import time


def f(x):
    print(x * x)
    time.sleep(2)
    return x * x


pool = Pool(processes=5)
res_list = []
for i in range(10):
    res = pool.apply(f, [i])

    print('______'), i
    res_list.append(res)

for r in res_list:
    print(r.get(timeout=1))
