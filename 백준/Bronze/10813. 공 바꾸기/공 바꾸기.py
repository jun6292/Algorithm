# https://www.acmicpc.net/problem/10813
# 백준 10813 공 바꾸기

# 바구니 1 ~ n, 공이 한개씩, 바구니에 적혀 있는 번호와 같은 번호가 적인 공이 들어 있음
# m번 공을 바꾸는데, 바구니 2개를 선택하고 그 안에 공을 교환
# 각 바구니에 어떤 공이 있는지 출력

n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a - 1], arr[b - 1] = arr[b - 1], arr[a - 1]

print(*arr)