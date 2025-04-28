# I 숫자 큐에 주어진 숫자를 삽입합니다.
# D 1	큐에서 최댓값을 삭제합니다.
# D -1	큐에서 최솟값을 삭제합니다.
# 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return

from heapq import heapify, heappush, heappop

def solution(operations):
    answer = []
    hq = []
    
    for op in operations:
        operation, number = op.split()
        number = int(number)
        
        if operation == 'I':
            heappush(hq, number)
        else:
            if len(hq) > 0:
                if number == -1:
                    heappop(hq)
                else:
                    hq.sort()
                    hq.pop()
    if len(hq) == 0:
        answer = [0, 0]
    else:
        hq.sort()
        answer = [hq[-1], hq[0]]
    
#     for operation in operations:
#         alphabet, number = operation.split()
#         number = int(number)

#         if alphabet == 'I':
#             heappush(hq, number)    
#         else:
#             if hq:
#                 if number == -1:
#                     heappop(hq)
#                 else:
#                     hq.sort()
#                     hq.pop()
                    
#     hq.sort()
#     if hq:
#         answer = [hq[-1], hq[0]]
#     else:
#         answer = [0, 0]
        
    return answer