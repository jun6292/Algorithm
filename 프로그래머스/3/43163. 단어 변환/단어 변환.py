from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        answer = 0
    else:
        answer = bfs(begin, target, words)
    return answer

def bfs(begin, target, words):
    queue = deque()
    queue.append([begin, 0])
    while queue:
        # 현재 단어와 현재 단계
        now, step = queue.popleft()
        
        if now == target:
            return step
        
        for word in words:
            cnt = 0
            # 단어 내 문자가 1개만 다른 경우
            for i in range(len(now)):
                if now[i] != word[i]:
                    cnt += 1
            if cnt == 1:
                queue.append([word, step + 1])