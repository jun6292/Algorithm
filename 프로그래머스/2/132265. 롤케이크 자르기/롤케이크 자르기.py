# 동일한 '가짓수'의 토핑이 올라가면 롤케이크가 공평하게 나눠짐
# 롤케이크를 공평하게 자르는 방법의 수를 return
# 공평하게 나눌 수 없으면 0
# 오른쪽에 토핑을 몰아넣고, 순회하면서 왼쪽에 토핑을 준다. 
# 왼쪽과 오른쪽과 같아지는 시점에서 answer += 1
from collections import Counter

def solution(topping):
    answer = 0
    right = Counter(topping)
    left = {}
    
    for i in range(len(topping) - 1):
        if topping[i] in left:
            left[topping[i]] += 1
        else:
            left[topping[i]] = 1
        
        right[topping[i]] -= 1
        
        if right[topping[i]] == 0:
            del right[topping[i]]
        
        if len(left) == len(right):
            answer += 1

    return answer