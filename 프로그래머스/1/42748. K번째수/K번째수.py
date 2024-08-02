def solution(array, commands):
    answer = []
    for c in commands:
        new_arr = array[c[0] - 1: c[1]]
        print(new_arr)
        new_arr.sort()
        answer.append(new_arr[c[2] - 1])
        
    return answer