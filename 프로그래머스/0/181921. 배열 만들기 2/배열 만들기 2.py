def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        i = str(i)
        for j in range(len(i)):
            if i[j] != '0' and i[j] != '5':
                break
        else:
            answer.append(int(i))
    if answer:
        answer.sort()
    else:
        answer.append(-1)
    return answer