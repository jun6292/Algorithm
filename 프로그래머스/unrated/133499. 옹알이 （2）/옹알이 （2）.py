# 중복 순열로 풀다가 실패
def solution(babbling):
    answer = 0
    babble = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in babble:
            if j + j not in i:
                i = i.replace(j, '#')
        if i.strip('#') == '':
            answer += 1
    return answer