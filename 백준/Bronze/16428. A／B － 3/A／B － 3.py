# https://www.acmicpc.net/problem/16428
# 백준 16428 A/B - 3

a, b = map(int, input().split())

q = a // b
r = a % b
if r < 0:
    q += 1
    r -= b

print(q)
print(r)

