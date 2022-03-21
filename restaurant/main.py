import math
import time


def task():
    chef = [2,2,5]
    customer = [4,5,6,30,123456789012]

    lcm_C = math.lcm(*chef)
    fx = []
    for i in range(lcm_C // min(chef)):
        for ti in chef:
            nti = i * ti
            if (nti < lcm_C):
                fx.append(nti)
    fx.sort()
    # print(lcm_C)
    # print(fx)
    len_fx = len(fx)
    for ci in customer:
        k = (ci-1) // len_fx
        x = (ci-1) % len_fx
        tt = k*lcm_C+fx[x]
        # print(f'{ci}: k={k} x={x} ans={tt}')

start = time.time_ns()

for _ in range(100000):
    task()

end = time.time_ns()

print(end)
print(start)
print((end-start) / 1e5)