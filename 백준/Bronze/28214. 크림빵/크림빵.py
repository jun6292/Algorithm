# https://www.acmicpc.net/problem/28214
# 크림빵 백준 28214

# 총 N개의 빵 묶음, K개의 빵 N x K
# 한 묶음에 P개 이상 크림 X -> 팔 수 없다

n, k, p = map(int, input().split())
tmp_list = list(map(int, input().split()))
arr = []

answer = 0
for i in range(0, len(tmp_list), k):
    arr.append(tmp_list[i : i + k])

for i in range(n):
    cnt = 0
    for j in range(k):
        if arr[i][j] == 0:
            cnt += 1

    if cnt < p:
        answer += 1

print(answer)
