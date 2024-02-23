def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(num):
        visited[num] = True
        for neighbor in range(n):
            if visited[neighbor] == False and computers[num][neighbor] == 1:
                dfs(neighbor)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer

