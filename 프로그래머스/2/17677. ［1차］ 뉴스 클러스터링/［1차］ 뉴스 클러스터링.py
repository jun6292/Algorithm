# 자카드 유사도 J(A, B): 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값
# (A & B) / (A | B)
# 두 집합이 모두 공집합일 경우, J(A, B) = 1
# 원소의 중복을 허용하는 다중집합의 경우 교집합은 min, 합집합은 max 갯수
# 문자열 사이의 유사도를 계산 -> 문자열을 두 글자씩 끊어서 다중집합 만들기
# 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다
# 대소문자 구분하지 않는다
# 유사도 값은 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력
# ---
# 먼저 두 문자열에 대해 각각 multi set 역할을 하는 딕셔너리를 만들자.
# key를 문자열로 value를 갯수로
# 두 딕셔너리를 순회하며 문제 조건에 맞는 합집합의 크기와 교집합의 크기를 구한 후 자카드 유사도를 구한다.

def is_alpha(ch):
    if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
        return True
    return False;

def make_dict_from_str(s):
    multi_dict = {}
    tmp = ''
    for i in range(len(s) - 1):
        if is_alpha(s[i]) and is_alpha(s[i + 1]):
            tmp = s[i].lower() + s[i + 1].lower()
            if tmp in multi_dict:
                multi_dict[tmp] += 1
            else:
                multi_dict[tmp] = 1
    return multi_dict

def solution(str1, str2):
    answer = 0
    multi_dict1, multi_dict2 = make_dict_from_str(str1), make_dict_from_str(str2)
    union_set_cnt, intersect_set_cnt = 0, 0
    
    for key, value in multi_dict1.items():
        if key in multi_dict2:  # 교집합
            if value > multi_dict2[key]:
                union_set_cnt += value
                intersect_set_cnt += multi_dict2[key]
            elif value < multi_dict2[key]:
                union_set_cnt += multi_dict2[key]
                intersect_set_cnt += value
            else:
                union_set_cnt += value
                intersect_set_cnt += value
        else:   # 합집합
            union_set_cnt += multi_dict1[key]
            
    for key, value in multi_dict2.items():
        if key not in multi_dict1.keys():
            union_set_cnt += multi_dict2[key]

    if union_set_cnt == 0:
        union_set_cnt, intersect_set_cnt = 1, 1
    
    print(intersect_set_cnt, union_set_cnt)
    answer = intersect_set_cnt / union_set_cnt
    print(answer)
    
    return (answer * 65536) // 1


