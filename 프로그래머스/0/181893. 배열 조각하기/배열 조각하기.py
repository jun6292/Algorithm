def solution(arr, query):
    answer = arr[:]
    for i in range(len(query)):
        if i % 2 == 0:   # 짝수 인덱스 -> 뒤를 버림
            answer = answer[:query[i] + 1]
        else:   # 홀수 인덱스 -> 앞을 버림
            answer = answer[query[i]:]
            
    return answer