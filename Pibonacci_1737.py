from collections import deque
from math import pi
n = int(input())

d = {n:0}
q = deque()
q.append(n)

while q:
    now = q.pop()
    if now <= pi and now >=0:
        d[now] = 1
    else:
        try:
            n1 = d[now - 1]
        except KeyError:
            d[now-1] = 0
            q.append(now)
            q.append(now - 1)
        try:
            n2 = d[now - pi]
        except KeyError:
            d[now-pi] = 0
            q.append(now)
            q.append(now - pi)
        try:
            d[now] = n1 + n2
        except NameError:
            continue

if n > pi:
    result = d[n-1] + d[n-pi]
else:
    result = 1

if result > 1e18:
    print(result % int(1e18))
else:
    print(result)
