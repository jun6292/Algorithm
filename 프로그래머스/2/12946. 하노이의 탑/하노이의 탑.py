def solution(n):
    answer = []
    hanoi(answer, n, 1, 3, 2)
    return answer

def hanoi(arr, n, src, dst, by):
    if n == 1:
        arr.append([src, dst])
    else:
        hanoi(arr, n - 1, src, by, dst)
        arr.append((src, dst))
        hanoi(arr, n - 1, by, dst, src)