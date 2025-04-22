# https://www.acmicpc.net/problem/2668
# 숫자고르기 백준 2668
# 사이클이 있는지 판단

import sys
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    num = int(input())
    arr[i].append(num)

def dfs(start, end):
    visited[end] = True

    for next_node in arr[end]:
        if not visited[next_node]:
            dfs(start, next_node)
        elif start == next_node:
            answer.append(start)
            return

answer = []
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    dfs(i, i)

answer.sort()
print(len(answer))
for i in answer:
    print(i)