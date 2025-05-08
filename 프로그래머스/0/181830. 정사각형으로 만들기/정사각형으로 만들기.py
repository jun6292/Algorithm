def solution(arr):
    answer = [[]]
    r = len(arr)
    c = len(arr[0])
    
    if r >= c:
        answer = [[0] * r for _ in range(r)]
    else:
        answer = [[0] * c for _ in range(c)]
    
    for i in range(r):
        for j in range(c):
            answer[i][j] = arr[i][j]
        
    return answer