# https://www.acmicpc.net/problem/17618
# 백준 17618 신기한 수

n = input()
answer = 0

for i in range(1, int(n) + 1):
    num_sum = 0
    str_i = str(i)
    for ch in str_i:
        num_sum += int(ch)
    if i % num_sum == 0:
        answer += 1

print(answer)