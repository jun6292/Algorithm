def solution(food):
    answer = ''
    for i in range(1, len(food)):
        for j in range(0, food[i] // 2):
            answer += str(i)
    tmp = answer
    answer += '0'
    answer += tmp[::-1]
    return answer