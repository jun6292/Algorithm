import heapq

# def solution(n, k, enemy):
#     answer = 0
#     e_heap = []
#     e_sum = 0
#     for i in enemy:
#         heapq.heappush(e_heap, i)
#         e_sum += i
#         if e_sum > n:
#             if k == 0:
#                 break
#             e_sum -= heapq.heappop(e_heap)
#             k -= 1
#         answer += 1
#     return answer

def solution(n, k, enemy):
    answer = 0
    e_heap = []
    e_sum = 0
    for i in enemy:
        heapq.heappush(e_heap, -i)
        e_sum += i
        if e_sum > n:
            if k == 0:
                break
            e_sum += heapq.heappop(e_heap)  
            k -= 1
        answer += 1
    return answer