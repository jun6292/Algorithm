from itertools import permutations

def solution(babbling):
    answer = 0
    babble = ['aya', 'ye', 'woo', 'ma']
    pron = []
    for i in range(1, len(babble) + 1):
        for j in permutations(babble, i):
            pron.append(''.join(j))
    
    for b in babbling:
        if b in pron:
            answer += 1
        
    return answer