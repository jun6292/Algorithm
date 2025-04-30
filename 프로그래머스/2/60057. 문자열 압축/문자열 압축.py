# 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현
# "aabbaccc"의 경우 "2a2ba3c"(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)
# 압축할 문자열 s, 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return
# 문자열은 제일 앞부터 정해진 길이만큼 잘라야 한다 good
# 완전탐색
def solution(s):
    answer = 1001
    # 1부터 s의 길이만큼 압축해보고 가장 짧은 문자열을 저장
    for i in range(1, len(s) + 1):
        answer = min(answer, len(compress(s, i)))
    return answer

def compress(string, num):
    tmp_str = string[:num]
    cnt = 1
    compressed_str = ""
    
    # 문자열은 제일 앞부터 정해진 길이만큼 자른다
    for i in range(num, len(string) + num, num):
        if tmp_str == string[i : i + num]:  # 중복 문자열이면
            cnt += 1
        else:   # 중복 문자열이 아님
            if cnt != 1:    # 중복 문자열이 있었으면
                compressed_str += (str(cnt) + tmp_str)
            else:
                compressed_str += tmp_str
            tmp_str = string[i : i + num]
            cnt = 1
    
    return compressed_str