def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        value = int(1e9)
        for i in range(s, e + 1):
            if arr[i] > k and value > arr[i]:
                value = arr[i]
        if value != int(1e9):
            answer.append(value)
        else:
            answer.append(-1)
        
    return answer