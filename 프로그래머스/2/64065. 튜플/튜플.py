# 중복되는 원소가 없는 튜플 / 원소의 구성이 같더라도 순서가 다르면 다른 튜플
# s가 표현하는 튜플을 배열에 담아 return
# 원소가 1개인 것 먼저 => {2}: 튜플의 맨 앞 원소 2
# 원소가 2개인 것 => {1, 2}: 순서가 바뀌었어도 튜플에서는 2, 1 순서임
# 원소가 3개인 것 => {3, 2, 1}: 튜플에서는 2, 1, 3
# 튜플 내부 원소의 순서를 생각할 때, 가장 많은 원소부터 앞에 온다.
# 즉, 원소의 개수를 기준으로 내림차순 정렬한 원소 리스트를 반환한다.

from collections import Counter

def solution(s):
    answer = []
    tmp = ''
    num_list = []
    
    for ch in s:
        if '0' <= ch <= '9':
            tmp += ch
        if tmp != '' and (ch == ',' or ch == '}'):
            num_list.append(int(tmp))
            tmp = ''
    
    sorted_list = sorted(Counter(num_list).items(), key=lambda x: -x[1])
    answer = [key for key, value in sorted_list]
    
    return answer