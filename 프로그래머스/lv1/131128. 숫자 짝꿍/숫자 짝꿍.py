def solution(X, Y):
    answer = []
    xDict = {}
    yDict = {}

    for x in X:
        xDict[x] = xDict.get(x, 0) + 1
    for y in Y:
        yDict[y] = yDict.get(y, 0) + 1

    # xDict의 key를 기준으로 탐색, 짝꿍이 있다면, xDict와 yDict에서 1을 빼고 answer에 추가
    for k, v in xDict.items():
        if k in yDict.keys():
            while yDict[k] > 0 and xDict[k] > 0:
                answer.append(k)
                yDict[k] = yDict.get(k) - 1
                xDict[k] = xDict.get(k) - 1

    # 짝꿍이 없을 때 return -1
    if (len(answer) == 0):
        return "-1"

    # 짝꿍이 0밖에 없을 경우 return 0
    if (answer.count('0') == len(answer)):
        return "0"

    answer.sort(reverse=True)   # default: 오름차순, reverse = True: 내림차순
    answer = ''.join(answer)    # 리스트를 문자열로 변경
    return answer