# 과제는 시작하기로 한 시각이 되면 시작
# 새로운 과제를 시작할 시각이 되었을 때, 기존에 진행 중이던 과제가 있다면 진행 중이던 과제를 멈추고 새로운 과제를 시작
# 진행중이던 과제를 끝냈을 때, 잠시 멈춘 과제가 있다면, 멈춰둔 과제를 이어서 진행
# 만약, 과제를 끝낸 시각에 새로 시작해야 되는 과제와 잠시 멈춰둔 과제가 모두 있다면, 새로 시작해야 하는 과제부터 진행
# 멈춰둔 과제가 여러 개일 경우, 가장 최근에 멈춘 과제부터 시작 => 스택
# 과제를 끝낸 순서대로 이름을 배열에 담아 return

# [name, start, playtime]
# 스택 활용

def solution(plans):
    answer = []
    st = []
    
    for i in range(len(plans)): # 시간을 정수로 변환
        h, m = map(int, plans[i][1].split(':'))
        plans[i][1] = h * 60 + m
        plans[i][2] = int(plans[i][2])
    
    plans.sort(key=lambda x: x[1])
    
    for i in range(len(plans) - 1):
        st.append([plans[i][0], plans[i][2]])
        time = plans[i + 1][1] - plans[i][1]    # 현재 과제와 다음 과제의 시간 차이
        
        while st and time > 0:
            if st[-1][1] > time:    # 현재 과제의 playtime이 더 크다 => playtime 감소 후 다음 과제 추가
                st[-1][1] -= time   # playtime 줄이고
                time = 0    # 다음 과제 시작
            else:   # 현재 과제의 playtime보다 작거나 같다 => 현재 과제 완료 후 다음 과제 전까지 진행 중인 과제 playtime 감소
                name, playtime = st.pop()   # 현재 과제 완료
                answer.append(name)
                time -= playtime    # 시간 차이 playtime만큼 감소
    
    answer.append(plans[-1][0])
    for i in range(len(st)):
        tmp = st.pop()
        answer.append(tmp[0])

    return answer