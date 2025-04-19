# https://www.acmicpc.net/problem/9625
# BABBA 백준 9625

k = int(input())
dp_a = [0] * (k + 1)
dp_b = [0] * (k + 1)
dp_a[0] = 1
dp_b[1] = 1

for i in range(2, k + 1):
    dp_a[i] = dp_a[i - 1] + dp_a[i - 2]
    dp_b[i] = dp_b[i - 1] + dp_b[i - 2]

print(dp_a[k], dp_b[k])