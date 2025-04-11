# https://www.acmicpc.net/problem/21611
# 백준 21611 마법사 상어와 블리자드

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

cy = cx = n // 2
cnt = flag = dr = 0
max_cnt = 1

# 왼쪽, 아래, 오른쪽, 위 / 좌하우상
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

pos = [] # 달팽이 좌표 저장 pos[] => 2차원 리스트를 1차원으로 처리
# 달팽이 좌표를 순서대로 pos[]에 저장
for _ in range(n * n - 1):
    cy, cx = cy + dy[dr], cx + dx[dr]
    pos.append((cy, cx))    # 2차원 달팽이 <-> 1차원 리스트 변환
    cnt += 1
    if cnt == max_cnt:
        cnt = 0
        dr = (dr + 1) % 4
        if flag == 0:
            flag = 1
        else:
            flag = 0
            max_cnt += 1

def bomb(lst):
    global answer
    nlst = []
    lst.append(-1)
    i = 0
    while i < len(lst) - 1:
        j = i + 1
        while lst[i] == lst[j]:
            j += 1
        if j - i >= 4:  # 폭발
            answer += lst[i] * (j - i)  # 구슬번호 * 폭발개수
        else:
            nlst += [lst[i]] * (j - i)  # 폭발 안했으면 리스트에 추가
        i = j

    lst.pop()
    return nlst

# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
answer = 0
for _ in range(m):
    d, s = map(int, input().split())

    # d 방향 s 거리만큼 0으로 수정 (arr), 1차원 리스트에 저장
    for mul in range(1, s + 1):
        arr[n // 2 + di[d - 1] * mul][n // 2 + dj[d - 1] * mul] = 0

    tmp_list = []   # 0이 아닌 실제 구슬만 저장
    for (i, j) in pos:
        if arr[i][j] > 0:
            tmp_list.append(arr[i][j])

    # 같은 번호 4개 연속 -> 사라짐
    while True:
        new_list = bomb(tmp_list)  # 4개 이상 폭발(점수 추가), 나머지
        if len(new_list) == len(tmp_list):  # 더 이상 폭발하지 않음
            break
        tmp_list = new_list

    # 구슬을 개수 + 구슬번호 형태로 변화
    tmp_list = []
    new_list.append(-1) # 마지막 데이터 처리를 위한 패딩 -> 나중에 제거 필요
    i = 0
    while i < len(new_list) - 1:
        j = i + 1
        while new_list[i] == new_list[j]:   # 구슬의 번호가 같으면 증가
            j += 1
        tmp_list += [(j - i), new_list[i]]  # 개수 + 번호 추가
        i = j

    # 2차원 배열에 복사
    arr = [[0] * n for _ in range(n)]
    for i in range(0, min(len(tmp_list), len(pos))):
        arr[pos[i][0]][pos[i][1]] = tmp_list[i]

print(answer)