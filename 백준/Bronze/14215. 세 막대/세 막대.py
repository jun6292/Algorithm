# https://www.acmicpc.net/problem/14215
# 백준 14215 세 막대

# 각 막대의 길이를 마음대로 줄일 수 있다.
# 삼각형이 되려면 두 막대의 합이 나머지 막대보다 커야한다.

arr = list(map(int, input().split()))
arr.sort()

a, b, c = arr

if a + b <= c:
    c = a + b - 1

print(a + b + c)