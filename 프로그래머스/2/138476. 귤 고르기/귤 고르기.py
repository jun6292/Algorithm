from collections import Counter
# 귤 k개를 고르는데, 서로 다른 종류의 수가 최소인 값을 반환
# tangerine 각각의 원소의 개수를 센 다음에 개수 순으로 내림차순 정렬
# k개가 될 때까지 앞에서부터 원소의 개수를 더해간다.

def solution(k, tangerine):
    different_type_cnt = 0
    tangerine_per_size = Counter(tangerine).most_common() # 개수 기준 내림차순 list로 반환
    tmp = 0
    
    for e in tangerine_per_size:
        tmp += e[1]
        different_type_cnt += 1
        
        if tmp >= k:
            break
            
    return different_type_cnt