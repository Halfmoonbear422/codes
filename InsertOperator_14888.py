'''
Solved! on Dec 29 2021
https://www.acmicpc.net/problem/14888
'''

from itertools import permutations as perm

n = int(input())
arr = list(map(int, input().split()))
# 0: +, 1: -, 2: *, 3: /
op = list(map(int, input().split()))

ops = []
for i in range(4):
    for _ in range(op[i]):
        ops.append(i)

mn = int(1e9)
mx = int(-1e9)

for op in set(perm(ops, n-1)):
    result = arr[0]
    for i in range(n - 1):
        if op[i] == 0:
            result += arr[i + 1]
        elif op[i] == 1:
            result -= arr[i + 1]
        elif op[i] == 2:
            result *= arr[i + 1]
        elif op[i] == 3:
            if result < 0:
                result = (-result // arr[i + 1]) * -1
            else:
                result = result // arr[i + 1]
    mn = min(mn, int(result))
    mx = max(mx, int(result))

print(mx)
print(mn)
