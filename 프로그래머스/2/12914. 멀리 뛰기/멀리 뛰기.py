# n = 1일 때, 1 = 1, 1가지
# n = 2일 때, 2 = 1 + 1 = 2, 2가지
# n = 3일 때, 3가지
# n = 4일 때, 5가지
# n = 5일 때, 8가지
# 결국 피보나치 수열 문제와 동등, DP 활용

def solution(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
        
    return dp[n] % 1234567
