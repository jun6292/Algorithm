# 참여가 가능한 학생 중 등수가 높은 3명을 선발
# 선발 고사 등수를 담은 정수 배열 rank와 전국 대회 참여 가능 여부가 담긴 boolean 배열 attendance
# 전국 대회에 선발된 학생 번호들을 등수가 높은 순서대로 각각 a, b, c번이라고 할 때 10000 × a + 100 × b + c를 return

def solution(rank, attendance):
    answer = 0
    arr = []
    
    idx = 0
    while idx < len(rank):
        if attendance[idx]:
            arr.append([rank[idx], idx, attendance[idx]])
        idx += 1
    arr.sort()
    
    rank_lst = []
    for i in range(3):
        rank_lst.append(arr[i])
    
    answer = rank_lst[0][1] * 10000 + rank_lst[1][1] * 100 + rank_lst[2][1]
    return answer