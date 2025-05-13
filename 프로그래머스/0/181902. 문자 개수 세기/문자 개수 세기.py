# A-Za-z
def solution(my_string):
    answer = [0] * 52
    alphabet =\
    [chr(a) for a in range(ord('A'), ord('Z') + 1)] + [chr(a) for a in range(ord('a'), ord('z') + 1)]
    # print(alphabet)
    for i in range(len(my_string)):
        answer[alphabet.index(my_string[i])] += 1        
        
    return answer