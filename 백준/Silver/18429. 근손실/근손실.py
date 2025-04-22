# https://www.acmicpc.net/problem/18429
# 근손실 백준 18429

# 500에서 하루가 지날때마다 k만큼 감소
# 하루에 1개씩 키트 사용, 중량 증가, n일 동안 한 번씩만 사용 가능
# 운동 기간동안 항상 중량이 500 이상으로 유지가 되도록 N일간의 운동 플랜을 세운다
# 항상 중량이 500 이상이 되도록 하는 경우의 수를 출력

n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

visited = [False] * n
def dfs(s, weight):
    global answer

    if weight < 500:
        return

    if s == n:
        answer += 1
        return

    weight -= k
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(s + 1, weight + arr[i])
            visited[i] = False

dfs(0, 500)
print(answer)