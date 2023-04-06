# 시간초과
# def solution(ingredient):
#     answer = 0
#     hamburger = '1231'  # 햄버거 1개
#     burger = ''.join(str(i) for i in ingredient)    # 정수 리스트 ingredient를 문자열로 변환
#     for i in ingredient:
#         if hamburger not in burger:
#             break
#         else:
#             burger = burger.replace(hamburger, '', 1)   # 발견되는 '1231'을 '#'로 변경
#             answer += 1
#     return answer

def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:  # 스택의 가장 마지막 4개 원소 
            answer += 1
            for _ in range(4):
                stack.pop()
    return answer