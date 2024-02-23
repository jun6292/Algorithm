answer = 0
def solution(numbers, target):
    dfs(numbers, 0, target, 0)
    return answer

def dfs(numbers, current, target, depth):
    global answer
    if depth == len(numbers):
        if target == current:
            answer += 1
        return
    
    dfs(numbers, current + numbers[depth], target, depth + 1)
    dfs(numbers, current - numbers[depth], target, depth + 1)
    
    