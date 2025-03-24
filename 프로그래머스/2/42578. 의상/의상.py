# 서로 다른 옷의 조합의 수를 return
# clothes에서 의상의 종류를 key로, 각 의상 종류의 개수를 value로 dictionary 만들기
# {"headgear": 2, "eyeware": 1}
# N, M, O, P, ... 이런식으로 숫자가 있을 때 한 종류 이상 반드시 포함해야 하는 경우의 수는 (N + 1)(M + 1)(O + 1)(P + 1)
# (N+1)에서 +1은 N이 없을 때를 나타낸다
# 하지만 항을 전개하다보면 마지막에 1이 나오는데, 이는 모두 포함하지 않는 것으로 1을 빼줘야 한다.

def solution(clothes):
    answer = 1
    clothes_dict = {cloth[1]: 0 for cloth in clothes}

    for cloth in clothes:
        clothes_dict[cloth[1]] += 1
    
    for v in clothes_dict.values():
        answer *= (v + 1)
    
    return answer - 1