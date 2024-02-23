def solution(tickets):
    visited = [False] * len(tickets)
    answer = []
    
    def dfs(start, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return
        
        for i, ticket in enumerate(tickets):
            if start == ticket[0] and visited[i] == False:
                visited[i] = True
                dfs(ticket[1], path + [ticket[1]])
                visited[i] = False
    
    dfs('ICN', ['ICN'])
    answer.sort()
    return answer[0]