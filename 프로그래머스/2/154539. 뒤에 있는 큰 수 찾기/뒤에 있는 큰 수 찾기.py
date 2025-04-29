# 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수를 뒷 큰수
# 모든 원소에 대한 뒷 큰수들을 차례로 담은 리스트 return
# 뒷 큰수가 존재하지 않는 원소의 경우 -1
def solution(numbers):
    answer = []
    n = len(numbers)
    answer = [-1] * n  # 뒷큰수를 저장할 배열, 초기값은 -1로 설정
    stack = []  # 현재까지 확인한 인덱스 저장

    for i in range(n - 1, -1, -1):
        while stack and numbers[i] >= numbers[stack[-1]]:
            stack.pop()
        if stack:
            answer[i] = numbers[stack[-1]]
        stack.append(i)
    return answer