# https://www.acmicpc.net/problem/21756
# 지우개 백준 21756
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(1, n + 1):
    arr.append(i)

while len(arr) > 1:
    tmp_arr = []
    for i in range(len(arr)):
        if i % 2 == 1:
            tmp_arr.append(arr[i])
    arr = tmp_arr[:]

print(arr[0])