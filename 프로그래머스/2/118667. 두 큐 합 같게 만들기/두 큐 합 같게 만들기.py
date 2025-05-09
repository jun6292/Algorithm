# 하나의 큐를 골라 원소를 추출(pop)하고, 추출된 원소를 다른 큐에 집어넣는(insert) 작업을 통해 각 큐의 원소 합이 같도록
# 작업의 최소 횟수를 return : 한 번의 pop과 한 번의 insert를 합쳐서 작업을 1회 수행한 것
# 어떤 방법으로도 각 큐의 원소 합을 같게 만들 수 없는 경우, -1을 return

# 길이가 같은 두 개의 큐
def solution(queue1, queue2):
    answer = 0
    total_sum = sum(queue1) + sum(queue2)
    if total_sum % 2 != 0:
        return -1
    
    target_sum = total_sum // 2
    start, end = 0, len(queue1) - 1
    cur_sum = sum(queue1)
    q = queue1 + queue2
    
    while cur_sum != target_sum:
        if cur_sum < target_sum:
            end += 1
            if end == len(queue1) * 2:
                return -1
            cur_sum += q[end]
        else:
            cur_sum -= q[start]
            start += 1
            
        answer += 1
        
    return answer