# 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s
# s가 의미하는 원래 숫자를 return
def solution(s):
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(arr)):
        idx = s.find(arr[i])
        if idx != -1:
            s = s.replace(arr[i], str(i))            
    
    return int(s)