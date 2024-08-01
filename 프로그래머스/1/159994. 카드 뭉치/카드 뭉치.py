def solution(cards1, cards2, goal):
    answer = ''
    cards1_len = len(cards1)
    cards2_len = len(cards2)
    goal_len = len(goal)
    cards1_idx = 0
    cards2_idx = 0
    cnt = 0
    for i in range(goal_len):
        if cards1_len > cards1_idx and goal[i] == cards1[cards1_idx]:
            cards1_idx += 1
            cnt += 1
        if cards2_len > cards2_idx and goal[i] == cards2[cards2_idx]:
            cards2_idx += 1
            cnt += 1
    if cnt < goal_len:
        answer = 'No'
    else:
        answer = "Yes"
            
    return answer