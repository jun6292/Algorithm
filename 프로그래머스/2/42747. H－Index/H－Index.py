def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    for idx, citation in enumerate(citations):
        if citation >= idx + 1:
            answer = idx + 1
    return answer