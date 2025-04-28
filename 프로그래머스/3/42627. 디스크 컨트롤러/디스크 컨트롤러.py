# 어떤 작업 요청이 들어왔을 때 [작업의 번호, 작업의 요청 시각, 작업의 소요 시간]을 저장해 두는 대기 큐가 있다. 처음에 이 큐는 비어있다.
# 하드디스크가 작업을 하고 있지 않고 대기 큐가 비어있지 않다면 가장 우선순위가 높은 작업을 대기 큐에서 꺼내서 하드디스크에 그 작업을 시킨다.
# 작업의 소요시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것 순으로 우선순위가 높다.
# 하드디스크는 작업을 한 번 시작하면 작업을 마칠 때까지 그 작업만 수행
# 하드디스크가 어떤 작업을 마치는 시점과 다른 작업 요청이 들어오는 시점이 겹친다면
# 요청이 들어온 작업을 대기 큐에 저장한 뒤 우선순위가 높은 작업을 대기 큐에서 꺼내서 하드디스크에 그 작업을 시킨다.
# 하드디스크가 어떤 작업을 마치는 시점에 다른 작업이 들어오지 않더라도 그 작업을 마치자마자 또 다른 작업을 시작할 수 있다
# ----
# 모든 요청 작업을 마쳤을 때
# 반환 시간(turnaround time)은 작업 요청부터 종료까지 걸린 시간으로 정의 / 반환 시간 = 작업 종료 시간 - 작업 요청 시간
# 모든 요청 작업의 반환 시간의 평균의 정수부분을 return

import heapq

# jobs: [작업이 요청되는 시점, 작업의 소요시간]
def solution(jobs):
    answer = 0
    turn_around = []    # [작업 종료 시간, 작업 요청 시간]
    hq = []     # 대기 큐
    time = 0    # 전체 시간 추적
    jobs.sort(key=lambda x: -x[0])   # 작업 요청 시간 역순으로 정렬 (jobs에서 pop의 효율성 제고)
    i = 0   # 작업번호
    
    while len(jobs) > 0 or len(hq) > 0:
        while len(jobs) > 0 and jobs[-1][0] <= time:
            start, duration = jobs.pop()
            # 소요시간이 짧은 것, 요청 시각이 빠른 것, 번호가 작은 것 순으로 우선순위가 높다.
            heapq.heappush(hq, [duration, start, i])
            i += 1
        
        if len(hq) > 0:
            du, st, pos = heapq.heappop(hq)
            time += du
            turn_around.append([time, st])
        else:
            time += 1

    total = 0
    for e, s in turn_around:
        total += e - s
    print(turn_around)
    answer = total // len(turn_around)
    return answer