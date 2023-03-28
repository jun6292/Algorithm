def solution(wallpaper):
    answer = []
    lux, luy, rdx, rdy = len(wallpaper), len(wallpaper[0]), 0, 0 
    for i in range(0, len(wallpaper)):
        for j in range(0, len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i)
                rdy = max(rdy, j)
    answer.append(lux)
    answer.extend([luy, rdx + 1, rdy + 1])
    print(answer)
    return answer