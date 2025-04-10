# https://www.acmicpc.net/problem/20056
# 백준 20056 마법사 상어와 파이어볼

# 격자 n x n, 파이어볼 m개, 이동 명령 k번
n, m, k = map(int, input().split())

# 파이어볼에 대한 정보 - [r, c, m, s, d]: 행, 열, 질량, 속도, 방향
fireball = [list(map(int, input().split())) for _ in range(m)]

# 상 우상 우 우하 하 좌하 좌 좌상
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

# 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결 => % n
# 마법사 상어가 k번 명령
for _ in range(k):
    # 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동
    for i in range(len(fireball)):
        r, c, m, s, d = fireball[i]
        r, c = (r + dy[d] * s) % n + 1, (c + dx[d] * s) % n + 1
        fireball[i] = r, c, m, s, d
    # 전체 원소 정렬(좌표 기준 정렬 -> 같은 좌표 처리)
    fireball.sort(key=lambda x: (x[0], x[1]))
    fireball.append([100, 100, 0, 0, 0])    # padding: 마지막 요소 처리 편의를 위해

    # 이동이 모두 끝난 뒤
    # 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다
    tmp_fireball = []
    i = 0   # 기준좌표
    while i < len(fireball) - 1:
        si, sj, m, s, d = fireball[i]
        direction_flag = 0  # 파이어볼의 방향 체크
        for j in range(i + 1, len(fireball)):
            if (si, sj) == (fireball[j][0], fireball[j][1]):    # 같은 좌표에 있으면 합친다
                m += fireball[j][2] # 질량 합치고
                s += fireball[j][3] # 속력 합치고
                if d % 2 != fireball[j][4] % 2: # (방향이 모두 짝수 or 모두 홀수)가 아닐 때
                    direction_flag = 1  # 홀수와 짝수가 섞여있으면 방향 1, 3, 5, 7 분배
            else:
                if j - i == 1:  # 같은 좌표에 없다 => 그냥 추가
                    tmp_fireball.append(fireball[i])
                else:   # 파이어볼은 4개의 파이어볼로 나누어진다
                    # 질량 (합쳐진 파이어볼 질량의 합 // 5)
                    if m // 5 > 0:  # 나눴을 때 1 이상
                        for dr in range(direction_flag, direction_flag + 8, 2):
                            tmp_fireball.append([si, sj, m // 5, s // (j - i), dr])
                i = j
                break
    fireball = tmp_fireball

answer = 0
for f in fireball:
    answer += f[2]

print(answer)
