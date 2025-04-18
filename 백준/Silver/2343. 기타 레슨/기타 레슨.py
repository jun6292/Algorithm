# https://www.acmicpc.net/problem/2343
# 기타레슨 백준 2343

# 블루레이의 크기는 모두 같아야 함, 기타 강의를 블루레이 안에 넣어야 함

# n: 강의의 수, m: 블루레이 수
n, m = map(int, input().split())

# 기타 강의의 길이가 강의 순서대로 -> 앞에서부터 차례대로 잘라야 한다
arr = list(map(int, input().split()))

left, right = max(arr), sum(arr)
while left <= right:
    mid = (left + right) // 2
    cnt, total = 1, 0

    for a in arr:
        if total + a <= mid:
            total += a
        else:
            total = a
            cnt += 1

    if m < cnt:
        left = mid + 1
    else:
        right = mid - 1

# 가능한 블루레이의 크기 중 최소 출력
print(left)
