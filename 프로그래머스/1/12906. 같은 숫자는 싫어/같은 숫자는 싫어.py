# 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거

def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
    return answer