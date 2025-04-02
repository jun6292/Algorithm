# https://www.acmicpc.net/problem/1312
# 백준 1312 소수

# 두 수를 나누었을 때, 소숫점 아래 N번째 자리수를 구한다.
# A=3, B=4, N=1이라면, A÷B=0.75 이므로 출력 값은 7
# A와 B(1 ≤ A, B ≤ 100,000), N(1 ≤ N ≤ 1,000,000)
# 0으로 나눌 경우를 고려하지 않아도 된다.
# 컴퓨터는 소숫점 아래 1,000,000 번째 자리까지 구하지 못할 것이다.

a, b, n = map(int, input().split())
answer = 0

for _ in range(n):
    a = a % b
    a *= 10
    answer = a // b

print(answer)