# https://www.acmicpc.net/problem/17608
# 막대기 백준 17608

# N개의 막대기 높이가 순서대로 주어질 때 오른쪽에서 보아서 몇 개가 보이는지 출력
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

answer = 1
max_height = arr[-1]
for i in range(len(arr) - 1, -1, -1):
    if arr[i] > max_height:
        max_height = arr[i]
        answer += 1

print(answer)