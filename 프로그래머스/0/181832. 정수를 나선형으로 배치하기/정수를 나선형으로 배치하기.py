def solution(n):
    answer = [[0] * n for _ in range(n)]
    i = flag = cnt = 1
    number = n ** 2
    cy = cx = dr = 0
    max_cnt = n
    
    # 우하좌상
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    while i <= number:
        answer[cy][cx] = i
        i += 1
        cy, cx = cy + dy[dr], cx + dx[dr]
        
        cnt += 1
        if cnt == max_cnt:
            cnt = 0
            dr = (dr + 1) % 4
            if flag == 1:
                flag = 0
                max_cnt -= 1
            else:
                flag = 1
            
    return answer