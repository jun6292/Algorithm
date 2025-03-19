# https://www.acmicpc.net/problem/1916
# 백준 1916 최소비용 구하기

# 최소 비용을 구한다 -> 다익스트라
from heapq import heappush, heappop

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]  # 노드(row) -> 노드(col)
INF = float("INF")
dist = [INF for _ in range(n + 1)]  # 노드(row) -> 노드 최소 비용 저장

for _ in range(m):
    start_num, end_num, cost = map(int, input().split())
    graph[start_num].append((end_num, cost))

start, end = map(int, input().split())

def dijkstra(s):
    visited = [False for _ in range(n + 1)] # 비용 업데이트 체크
    q = [(0, s)]    # (비용, 시작 노드) -> heap에 넣을 거기 때문에 비용을 앞에
    dist[s] = 0     # 시작 노드 비용 초기화

    while q:
        d, v = heappop(q)
        if visited[v]:   # 이미 비용이 업데이트된거라면 넘어감
            continue

        visited[v] = True
        for i, nv in graph[v]:  # i: 도착 노드, nv: 비용
            distance = d + nv   # 이전 노드의 비용 + 비용
            if distance < dist[i]:  # 새로 거리 계산한 것 < 기존 거리
                dist[i] = distance  # 더 작은 값으로 비용 업데이트
                heappush(q, (distance, i))  # minheap 작은 순서로 정렬

dijkstra(start)
print(dist[end])