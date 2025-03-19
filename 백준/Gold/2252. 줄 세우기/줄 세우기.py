# 백준 2252 줄 세우기
# https://www.acmicpc.net/problem/2252
# 위상정렬
# 1번이 2번 앞에 서야 한다. 1 -> 2
# 1번이 3번 앞에 서야 한다. 1 -> 3
# 2, 3의 진입차수 각각 1씩

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]   # 노드 -> 노드
indeg = [0 for _ in range(n + 1)] # 진입 차수
q = deque()
result = []

for _ in range(m):
    a, b = map(int, input().split())    # a가 b 앞에 서야 한다
    graph[a].append(b)
    indeg[b] += 1 # b의 진입 차수 1 증가

for i in range(1, n + 1):
    if indeg[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    result.append(node)

    for j in graph[node]:
        indeg[j] -= 1
        if indeg[j] == 0:
            q.append(j)

print(*result)