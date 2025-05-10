def solution(picture, k):
    answer = []
    row = len(picture)
    col = len(picture[0])
    
    for i in range(row):
        tmp = ''
        for j in range(col):
            tmp += picture[i][j] * k
        for num in range(k):
            answer.append(tmp)
    
    return answer