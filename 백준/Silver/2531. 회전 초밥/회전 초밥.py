# https://www.acmicpc.net/problem/2531
# 회전 초밥 백준 2531

# 초밥의 종류 -> 번호, 같은 초밥 둘 이상 있을 수 있음
# 1) 한 위치부터 k개 연속해서 먹기
# 2) 초밥의 종류 하나가 쓰인 쿠폰 발행, 쿠폰 초밥 하나 무료 제공
# - 없으면 새로 만들어 제공
# 초밥 가짓수의 최댓값 구하기
answer = 0

# n: 초밥 수, d: 초밥 가짓수, k: 연속해서 먹는 접시 수, c: 쿠폰 번호
n, d, k, c = map(int, input().split())

arr = [int(input()) for _ in range(n)]
arr = arr + arr

for i in range(len(arr) // 2):
    sushi = set(arr[i : i+k])
    sushi.add(c)
    answer = max(answer, len(sushi))

print(answer)
