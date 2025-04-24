# 정확하게 순위를 매길 수 있는 선수의 수를 return
# [A, B]는 A 선수가 B 선수를 이겼다는 의미

def solution(n, results):
    answer = 0
    arr = [[0] * (n + 1) for _ in range(n + 1)]
    
    for a, b in results:
        arr[a][b] = 1
    
    # 플로이드 워셜
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if arr[i][j] == 0 and arr[i][k] == 1 and arr[k][j] == 1:
                    arr[i][j] = 1
    
    # 한 사람에 대한 경기 결과가 n - 1개이면 순위 결정 가능
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i][j] == 1:
                result[i] += 1
                result[j] += 1
    print(result)
    for i in range(1, n + 1):
        if result[i] == n - 1:
            answer += 1
    
    return answer