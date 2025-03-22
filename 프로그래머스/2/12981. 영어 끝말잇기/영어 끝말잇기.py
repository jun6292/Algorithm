# [가장 먼저 탈락하는 사람 번호, 몇 번째 차례인지]
# 앞 단어의 마지막 글자와 바로 뒤 단어의 첫 글자가 다를 때
# 중복 단어가 나왔을 때
import math

def solution(n, words):
    answer = []
    word_dict = {}
    wrong_idx = 0
    
    for word in words:
        word_dict[word] = 0
    
    word_dict[words[0]] += 1
    
    for i in range(1, len(words)):
        word_dict[words[i]] += 1
        if words[i - 1][-1] != words[i][0]:
            wrong_idx = i
            break
        if word_dict[words[i]] > 1:
            wrong_idx = i
            break
    
    if wrong_idx == 0:
        answer.append(0)
        answer.append(0)
    else:
        person = ((wrong_idx) % n) + 1
        order = math.ceil(((wrong_idx + 1) / n))
        answer.append(person)
        answer.append(order)
        
    return answer