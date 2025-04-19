# https://www.acmicpc.net/problem/1904
# 01타일 백준 1904

n = int(input())
a, b = 1, 1

for i in range(2, n + 1):
    a, b = b, (a + b) % 15746

print(b)