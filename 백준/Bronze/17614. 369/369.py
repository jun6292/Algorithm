# https://www.acmicpc.net/problem/17614
# 369 백준 17614

# 원형, 1부터 시작, 시계방향으로 돌아가며 1씩 증가
# 3, 6, 9가 포함되어 있지 않으면 말하기 / 3, 6, 9가 포함되면 개수만큼 박수
# 박수의 총 횟수를 출력

# 입력 n의 최대 크기가 100만 이므로 for문 한번 돌면 끝

check = ['3', '6', '9']
n = int(input())
answer = 0

for num in range(1, n + 1):
    str_num = str(num)
    for c in check:
        answer += str_num.count(c)

print(answer)

