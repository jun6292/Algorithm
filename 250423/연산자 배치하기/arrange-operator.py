# https://www.acmicpc.net/problem/14888
# https://www.codetree.ai/ko/frequent-problems/problems/arrange-operator/description
# 백준 14888 연산자 끼워넣기
# 코드트리 연산자 배치하기

n = int(input())
numbers = list(map(int, input().split()))
calc = list(map(int, input().split()))
max_value, min_value = -float("INF"), float("INF")

visited = [False] * n
def dfs(num, depth):
    global max_value, min_value

    if depth == n:
        max_value, min_value = max(max_value, num), min(min_value, num)
        return

    for i in range(3):
        if calc[i] != 0:
            calc[i] -= 1
            if i == 0:
                result = num + numbers[depth]
            elif i == 1:
                result = num - numbers[depth]
            elif i == 2:
                result = num * numbers[depth]
            dfs(result, depth + 1)
            calc[i] += 1

dfs(numbers[0], 1)

print(min_value, max_value)