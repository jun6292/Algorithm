def solution(n, k):
    dc = 0
    if n >= 10:
        dc = n // 10
    answer = 12000 * n + 2000 * (k - dc)
    return answer