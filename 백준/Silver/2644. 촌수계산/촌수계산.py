# https://www.acmicpc.net/problem/2644
# 촌수계산 백준 2644

# 부모와 자식 사이를 1촌으로 정의
# 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌
# 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌
# 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산
# 입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력
# 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때는 -1을 출력

import sys
input = sys.stdin.readline

n = int(input())    # 사람 수
start, end = map(int, input().split())    # 촌수를 계산해야 되는 두 사람
m = int(input())    # 부모 자식들 간의 관계의 개수
arr = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [-1] * (n + 1)
visited[start] = 0
def dfs(node):
    if node == end:
        return

    for n_node in arr[node]:
        if visited[n_node] == -1:   # 미방문
            visited[n_node] = visited[node] + 1
            dfs(n_node)

dfs(start)
print(visited[end])