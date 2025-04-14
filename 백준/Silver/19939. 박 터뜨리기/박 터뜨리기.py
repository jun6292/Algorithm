# https://www.acmicpc.net/problem/19939
# 박 터뜨리기 백준 19939

# N개의 공을 K개의 바구니에 빠짐없이 나누어 담는데,
# 각 바구니에는 1개 이상의 공이 있어야 하고, 바구니에 담긴 공의 개수가 모두 달라야 한다.
# 가장 많이 담긴 바구니와 가장 적게 담긴 바구니의 공의 개수 차이가 최소가 되도록

# n: 공의 개수, k: 팀의 수
n, k = map(int, input().split())
basket = [0] * (k + 1)
ball = n

for i in range(1, k + 1):
    basket[i] = i
    ball -= i

if ball < 0:
    print(-1)
else:
    while ball > 0:
        for i in range(k, 0, -1):
            basket[i] += 1
            ball -= 1
            if ball == 0:
                break
    print(basket[k] - basket[1])