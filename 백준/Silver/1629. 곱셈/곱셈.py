# https://www.acmicpc.net/problem/1629
# 백준 1629 곱셈
# '자연수 A를 B번 곱한 수'를 C로 나눈 나머지를 구하라.
# 분할정복
def solve(a, b):
    if b == 1:
        return a % c

    result = solve(a, b // 2)

    if b % 2 == 0:
        return (result * result) % c
    else:
        return (result * result * a) % c

A, B, c = map(int, input().split())
print(solve(A, B))