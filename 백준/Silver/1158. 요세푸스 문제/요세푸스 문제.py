# https://www.acmicpc.net/problem/1158
# 요세푸스 문제 백준 1158

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다.
# 순서대로 K번재 사람을 제거
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 N명의 사람이 모두 제거될 때까지 계속

n, k = map(int, input().split())
arr = [i for i in range(1, n + 1)]
lst = []

idx = k - 1
while arr:
    tmp = arr.pop(idx % len(arr))
    lst.append(tmp)
    if len(arr) == 0:
        break
    idx += (k - 1)
    idx = idx % len(arr)

answer = '<'
for i in range(len(lst)):
    answer += str(lst[i])
    if i != len(lst) - 1:
        answer += ', '
answer += '>'

print(answer)