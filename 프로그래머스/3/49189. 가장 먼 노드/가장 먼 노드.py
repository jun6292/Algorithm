# 1번 노드에서 가장 멀리 떨어진 노드의 갯수 (최단거리)

from collections import deque

def bfs(n, start, arr):
    q = deque()
    visited = [0] * (n + 1)
    
    q.append(start)
    visited[start] = 1
    
    while q:
        node = q.popleft()
        for next_node in arr[node]:
            if visited[next_node] == 0:
                q.append(next_node)
                visited[next_node] = visited[node] + 1

    return visited

def solution(n, edge):
    answer = 0
    arr = [[] for _ in range(n + 1)]
    
    for i in range(len(edge)):
        arr[edge[i][1]].append(edge[i][0])
        arr[edge[i][0]].append(edge[i][1])
    
    node_list = bfs(n, 1, arr)
    max_value = max(node_list)
    answer = node_list.count(max_value)
    
    return answer