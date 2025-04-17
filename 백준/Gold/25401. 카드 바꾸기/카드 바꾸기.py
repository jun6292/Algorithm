# https://www.acmicpc.net/problem/25401
# 카드 바꾸기 백준 25401

n = int(input())
arr = [0] + list(map(int, input().split()))
answer = 500

# 바꿀 카드의 갯수를 확인
def check(s, diff):
    cnt = 0
    for i in range(1, n + 1):
        s += diff
        if arr[i] != s:
            cnt += 1
    return cnt

# 최대 바꿀 수 있는 카드의 숫자는 n - 2
for i in range(1, n):
    for j in range(i + 1, n + 1):
        diff = (arr[j] - arr[i]) / (j - i)

        if diff - int(diff) != 0:
            continue

        answer = min(answer, check(arr[i] - diff * i, diff))

print(answer)
