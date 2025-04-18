# https://www.acmicpc.net/problem/11726
# 2×n 타일링 백준 11726

# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하라
# 피보나치 수열과 똑같다

n = int(input())

dp = [0] * (n + 1)

dp[0] = dp[1] = 1
for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[n] % 10007)