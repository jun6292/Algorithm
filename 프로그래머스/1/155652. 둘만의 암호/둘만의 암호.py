# 문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꾼다.
# index만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로
# skip에 있는 알파벳은 제외하고 건너뛴다.
# s를 변환한 결과를 return

def solution(s, skip, index):
    answer = ''
    alphabet = []
    for i in range(26):
        tmp = chr(ord('a') + i)
        if tmp in skip:
            continue
        else:
            alphabet.append(tmp)
    for i in range(len(s)):
        print((alphabet.index(s[i]) + index) % (26 - len(skip)))
        answer += alphabet[(alphabet.index(s[i]) + index) % (26 - len(skip))]
    return answer