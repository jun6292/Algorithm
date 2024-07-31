def solution(n):
    answer = []
    num_list = list(str(n))
    for i in range(len(num_list) - 1, -1, -1):
        answer.append(int(num_list[i]))
    
    return answer