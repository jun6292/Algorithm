# 게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이
# 좌표평면의 경계를 넘어가는 명령어는 무시

def solution(dirs):
    answer = 0
    cy, cx = 5, 5
    path = set()
    
    for i in range(len(dirs)):
        if dirs[i] == 'L':
            ny, nx = cy, cx - 1
        if dirs[i] == 'R':
            ny, nx = cy, cx + 1
        if dirs[i] == 'D':
            ny, nx = cy + 1, cx
        if dirs[i] == 'U':
            ny, nx = cy - 1, cx
        
        if 0 <= ny < 11 and 0 <= nx < 11:
            if ((cy, cx), (ny, nx)) not in path:
                path.add(((cy, cx), (ny, nx)))
                path.add(((ny, nx), (cy, cx)))
                answer += 1
            cy, cx = ny, nx
        else:
            continue
    
    return answer