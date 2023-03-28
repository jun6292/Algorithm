from collections import defaultdict

def solution(id_list, report, k):
    answer = [] 
    # key error 방지
    report_cnt = defaultdict(int) 
    report_map = defaultdict(set) 
    report = list(set(report))  
    
    for s in report:
        first, second = s.split()   
        report_map[first].add(second)
        report_cnt[second] += 1 
    
    for i in id_list:
        result = 0
        for j in report_map[i]:
            if report_cnt[j] >= k:
                result += 1
        answer.append(result)
    
    return answer