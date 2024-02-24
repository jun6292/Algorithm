from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    for i in permutations(dungeons, len(dungeons)):
        stamina = k
        cnt = 0
        
        for need, use in i:
            if stamina >= need:
                stamina -= use
                cnt += 1
        answer = max(answer, cnt)
    return answer