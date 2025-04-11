# https://www.acmicpc.net/problem/23290
# https://www.codetree.ai/ko/frequent-problems/problems/pacman/description
# 백준 23290 마법사 상어와 복제
# 코드트리 팩맨

# 물고기 m 마리, 각 물고기는 이동 방향을 가지고 있다
# 둘 이상의 물고기가 같은 칸에 있을 수 있고, 마법사 상어와 물고기가 같은 칸에 있을 수 있다
# 1) 물고기 복제 시전, but 5번에서 복제됨
# 2) 물고기 이동, 상어가 있는 칸 + 물고기 냄새 있는 칸 + 격자 범위 밖 이동 불가
# - 이동할 수 없으면 45도 반시계 회전, 그래도 없으면 이동 안함
# 3) 상어가 연속 3칸 이동, 상하좌우로 이동, 범위내, 물고기가 있는 칸으로 이동하면 물고기 제외, 물고기 냄새 남김
# - 물고기가 가장 많이 제외되는 방법으로 이동, 여러가지 인 경우 사전 순
# 4) 2턴이 지나면 물고기 냄새 사라짐
# 5) 복제 완료, 1에서의 위치와 방향을 그대로 가짐

# 물고기 수, 마법 연습 횟수
m, s = map(int, input().split())
fish = []
for _ in range(m):
    i, j, dr = map(int, input().split())
    # [0]: 행 [1]: 열 [2]: 방향 [3]: 물고기 수
    fish.append([i - 1, j - 1, dr - 1, 1])

# 8방향: 1~8 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 좌 좌상 상 우상 우 우하 하 좌하 -> 시계 방향
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

# 최초 상어 위치
sy, sx = map(int, input().split())
sy, sx = sy - 1, sx - 1

visited = [[0] * 4 for _ in range(4)]   # 물고기 냄새 표시
# 4 x 4 좌표 set에 넣어 놓기 -> 시간 복잡도 고려
boundary = set([(i, j) for j in range(4) for i in range(4)])

def move_fish():
    # 물고기 이동 - 상어 X, 범위 내, 냄새 X, 방향은 반시계 45도
    for i in range(len(fish)):
        ci, cj, dr, cnt = fish[i]
        # 반시계 방향(감소, -1)으로 8방향 체크
        for d in range(8):
            ni, nj = ci + dy[(dr - d + 8) % 8], cj + dx[(dr - d + 8) % 8]
            if (ni, nj) != (sy, sx) and (ni, nj) in boundary and visited[ni][nj] == 0:
                fish[i] = [ni, nj, (dr - d + 8) % 8, cnt]
                break   # 한번 이동하면 끝

def shark():
    max_fish = -1 # 무조건 갱신될 최악의 값으로 초기화
    del_set = set()
    # 3) 상어 3칸 연속이동, 상어 위치 물고기 삭제 및 냄새 남기기(3)
    # 상(1) -> 좌(2) -> 하(3) -> 우(4) : 사전순
    for d1 in (2, 0, 6, 4):
        i1, j1 = sy + dy[d1], sx + dx[d1]
        if (i1, j1) not in boundary:    # 범위 밖이면 다음 방향
            continue
        for d2 in (2, 0, 6, 4):
            i2, j2 = i1 + dy[d2], j1 + dx[d2]
            if (i2, j2) not in boundary:
                continue
            for d3 in (2, 0, 6, 4):
                i3, j3 = i2 + dy[d3], j2 + dx[d3]
                if (i3, j3) not in boundary:
                    continue
                fish_cnt = 0
                shark_set = {(i1, j1), (i2, j2), (i3, j3)}
                for i, j, dr, cnt in fish:
                    if (i, j) in shark_set: # 상어의 연속 3칸 이동과 같은 좌표면...
                        fish_cnt += cnt
                if max_fish < fish_cnt:
                    max_fish, ni, nj = fish_cnt, i3, j3
                    del_set = shark_set     # 삭제할 좌표 후보
    # 물고기 삭제 후 냄새(3) 남기기
    for i in range(len(fish) - 1, -1, -1):
        if (fish[i][0], fish[i][1]) in del_set:
            visited[fish[i][0]][fish[i][1]] = 3
            fish.pop(i)

    # 상어 최종 좌표 return
    return ni, nj

def merge(fish):
    # 복제된 물고기와 기존 물고기 합치기
    # 같은 좌표, 같은 방향의 물고기 군집 누적
    fish.sort(key=lambda x:(x[0], x[1], x[2]))

    i = 1
    while i < len(fish):
        if fish[i - 1][:3] == fish[i][:3]:  # 좌표, 방향 같으면
            fish[i - 1][3] += fish[i][3]
            fish.pop(i)
        else:
            i += 1

for _ in range(s):
    # 1) 물고기 복제
    new_fish = [x[:] for x in fish]

    # 2) 모든 물고기 한 칸 이동
    move_fish()

    # 3) 상어 3칸 연속이동, 상어 위치 물고기 삭제 및 냄새 남기기(3)
    sy, sx = shark()

    # 4) 물고기 냄새 - 1
    for i in range(4):
        for j in range(4):
            if visited[i][j] > 0:
                visited[i][j] -= 1

    # 5) 복제된 물고기와 기존 물고기 합치기
    fish += new_fish
    merge(fish)    # 같은 좌표, 같은 방향의 물고기 합치고 개수 증가 후 물고기 삭제


answer = 0
for i in range(len(fish)):
    answer += fish[i][3]
print(answer)

# 사전 순: 방향을 정수로 변환. 상은 1, 좌는 2, 하는 3, 우는 4로 변환하고 수를 이어 붙여 정수로 하나 만든다.
# 두 방법 A와 B가 있고, 각각을 정수로 변환한 값을 a와 b라고 하자. a < b를 만족하면 A가 B보다 사전 순으로 앞선 것

# (4 x 4 격자) * (100 턴) * (64 경우의 수 - 상어 이동 조합) * (10^6 물고기) => 시간 복잡도 터짐
# 64 경우의 수를 군집으로 처리해야 한다