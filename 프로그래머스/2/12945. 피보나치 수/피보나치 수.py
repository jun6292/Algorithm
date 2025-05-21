def solution(n):
    fibo = [0] * n
    fibo[0], fibo[1] = 1, 1
    mod = 1234567
    for i in range(2, n):
        fibo[i] = fibo[i - 1] % mod + fibo[i - 2] % mod
    return fibo[n - 1] % mod