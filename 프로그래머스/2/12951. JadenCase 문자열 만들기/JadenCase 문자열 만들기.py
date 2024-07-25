def solution(s):
    answer = []
    if 'a' <= s[0] <= 'z':
        answer.append(s[0].upper())
    else:
        answer.append(s[0])
    for i in range(1, len(s)):
        if '0' <= s[i] <= '9':
            answer.append(s[i])
        elif s[i - 1] == ' ' and s[i] != ' ':
            answer.append(s[i].upper())
        else:
            answer.append(s[i].lower())
    return ''.join(answer)