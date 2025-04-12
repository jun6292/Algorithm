# https://www.acmicpc.net/problem/21609
# 백준 21609 상어 중학교
# https://www.codetree.ai/ko/frequent-problems/problems/colored-bomb/description
# 코드트리 색깔폭탄

# 초기 격자의 모든 칸에는 블록이 있다 - 검(-1), 무지개(0), 일반(m 이하의 자연수)
# 상하좌우만 인접한 칸
# 블록 그룹: 연결된 블록 집합, 일반 블록 적어도 하나 이상, 일반 블록 색은 모두 같아야
# - 검은색 블록은 X, 무지개 블록은 상관 없다, 블록 개수는 2보다 크거나 같아야 한다
# - 그룹 안의 블록은 인접한 칸으로 이동해서 그룹의 모든 칸으로 이동할 수 있어야 한다
# - 기준 블록은 무지개 블록이 아닌 행/열 기준 번호가 가장 작은 일반 블록
# 오토 플레이 => 블록 그룹이 존재하는 동안 계속해서 반복
# 1) 크기가 가장 큰 블록 그룹을 찾는다.
# - 여러 개일 경우, 무지개 블록의 수가 가장 많은 블록 그룹, 기준 블록 행 크고, 열 큰 것
# 2) 1에서 찾은 블록 그룹의 모든 블록을 제거, 블록의 수를 B라 했을 때 B^2점 획득
# 3) 중력 작용
# 4) 격자가 90도 반시계로 회전
# 5) 중력 작용
# 중력 작용 시 검은색 블록을 제외한 모든 블록이 행 번호가 큰 칸으로 이동
# - 중력은 검은색 블록에 작용하지 않는다.
# 오토 플레이가 모두 끝났을 때 획득한 점수의 합 출력

from collections import deque

n, m = map(int, input().split())
empty = m + 1   # 빈칸 표시: m + 1

# 4방향을 -1로 둘러싸서 범위 체크 안하기 위함
arr = [[-1] * (n + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(n)] + [[-1] * (n + 2)]

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 같은 색깔 블럭(color)이거나 무지개(0) 색깔, rainbow_cnt += 1, v[] 표시 -> 일반, group 표시 -> 무지개, 일반
def bfs():
    # 미방문 일반 블록에서 bfs 확산(가장 큰 크기, 우선순위)
    visited = [[0] * (n + 2) for _ in range(n + 2)]
    max_group = set()
    max_rainbow_cnt = 0
    for si in range(1, n + 1):
        for sj in range(1, n + 1):
            if visited[si][sj] == 0 and 0 < arr[si][sj] <= m:   # 미방문, 일반 블럭
                q = deque()
                group = set()
                rainbow_cnt = 0

                q.append((si, sj))
                group.add((si, sj))
                visited[si][sj] = 1
                color = arr[si][sj] # 같은 색깔 블록을 위해

                while q:
                    ci, cj = q.popleft()
                    # 4방향
                    for dr in range(4):
                        ni, nj = ci + dy[dr], cj + dx[dr]
                        # 미방문(같은 색깔 or 무지개 블럭)
                        if visited[ni][nj] == 0 and (ni, nj) not in group and (arr[ni][nj] == color or arr[ni][nj] == 0):
                            q.append((ni, nj))
                            group.add((ni, nj))
                            if arr[ni][nj] == 0:    # 무지개 블록이면 visited와 따로 표시
                                rainbow_cnt += 1
                            else:
                                visited[ni][nj] = 1
                # 그룹 개수 > 같으면 rainbow_cnt 큰 값 > 행 > 역
                if len(max_group) < len(group) or (len(max_group) == len(group) and max_rainbow_cnt <= rainbow_cnt):
                    max_group, max_rainbow_cnt = group, rainbow_cnt

    return max_group

# 중력: 블록(일반 + 무지개) and 밑칸 빈칸 -> 둘이 교환, 좌표 끝에서부터 감소시키면서
def gravity():
    for si in range(1, n):  # 맨 끝 행은 중력 X
        for sj in range(1, n + 1):  # 열은 모두 중력 받음
            ci, cj = si, sj
            # (ci, cj) 위치가 블록(일반: 1 ~ m, 무지개: 0)이고, 아래칸이 빈칸이면 교환(위로 반복)
            while 0 <= arr[ci][cj] <= m and arr[ci + 1][cj] == empty:
                arr[ci][cj], arr[ci + 1][cj] = arr[ci + 1][cj], arr[ci][cj]
                ci -= 1     # 위로 한칸씩 올라가며 수행

answer = 0
while True:
    # 미방문 일반 블럭 bfs로 그룹(set) 찾기, bfs에서 set 만들때는 미방문이 조금 다름
    # 지울 그룹
    block_group = bfs()

    # 그룹에 속한 블록의 개수는 2보다 크거나 같아야 한다.
    if len(block_group) < 2:    # 그룹 안의 블록 개수가 2개 미만이면 종료
        break

    answer += len(block_group) ** 2  # 점수에 추가
    # 선택한 블럭 그룹 삭제
    for ty, tx in block_group:
        arr[ty][tx] = empty

    # 중력 처리
    gravity()

    # 반시계 방향 90도 회전
    arr = list(map(list, zip(*arr)))[::-1]

    # 중력 처리
    gravity()

print(answer)

