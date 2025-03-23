# elements 배열의 길이가 1000 이하이므로 O(N^2)의 시간복잡도로 해결해도 시간 초과가 나지 않을 것이다.
# 연속 부분수열이므로 % 연산을 하던가, 리스트를 붙여서 이중 for문을 돌리자
# 마지막에 set으로 중복을 제거해준 뒤, 원소의 갯수를 세서 반환
def solution(elements):
    arr = []
    elements_len = len(elements)    # 5
    elements = elements + elements  # [7, 9, 1, 1, 4, 7, 9, 1, 1, 4]
    
    for i in range(1, elements_len + 1):
        start, end = 0, i
        for _ in range(elements_len):
            tmp = sum(elements[start:end])
            arr.append(tmp)
            start += 1
            end += 1

    return len(set(arr))