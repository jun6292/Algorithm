# 순간이동 (현재까지 온 거리 * 2) -> 건전지 사용 X
# K 칸 점프 -> K 만큼의 배터리 사용
# 점프로 이동하는 것을 최소화하자. 즉, 건전지 사용량의 최솟값을 구하자.
# 0(1) -> 1 -> 2 까지 배터리 1소요
# 0(1) -> 1 -> 2(1) -> 3 까지 배터리 2소요
# n부터 0까지 가는 것으로 생각, n이 홀수면 1칸 뒤로 이동 -> 배터리 +1
# n이 짝수면 절반으로 나누기, 배터리 소모 X
def solution(n):
    min_battery_usage = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2
            continue
        else:
            n -= 1
            min_battery_usage += 1

    return min_battery_usage