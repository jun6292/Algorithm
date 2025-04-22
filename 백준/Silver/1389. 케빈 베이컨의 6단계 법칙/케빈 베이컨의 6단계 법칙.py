# https://www.acmicpc.net/problem/1389
# 케빈 베이컨의 6단계 법칙 백준 1389

# 임의의 두 사람이 최소 몇 단계 만에 이어질 수 있는지 계산
# 단계의 총 합이 가장 적은 사람

# 케빈 베이컨의 수가 가장 작은 사람 중에서도 번호가 가장 작은 사람
# 친구가 한 명도 없는 사람은 없다 -> 모든 노드는 간선으로 연결되어 있음

from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
kevin = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

def bfs(start, end):
    visited = [0] * (n + 1)

    q = deque()
    q.append(start)

    while q:
        node = q.popleft()
        if node == end:
            return visited[node]
        for nn in arr[node]:
            if visited[nn] == 0:
                q.append(nn)
                visited[nn] = visited[node] + 1

    # 도달하지 말아야 할 부분
    return -1

for i in range(1, len(arr) - 1):
    for j in range(i + 1, len(arr)):
        kevin[i][j] = kevin[j][i] = bfs(i, j)

answer = []
for i in range(1, n + 1):
    answer.append((i, sum(kevin[i])))

answer.sort(key=lambda x: (x[1], x[0]))
print(answer[0][0])