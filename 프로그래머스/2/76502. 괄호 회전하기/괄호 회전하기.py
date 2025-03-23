# 문자열 s를 0부터 (s - 1)칸만큼 회전 시킨 후 스택 이용
# 왼쪽 괄호면 스택에 push, 오른쪽 괄호면 스택 top과 비교 후 pop 결정
left = ['[', '{', '(']

def solution(s):
    answer = 0
    arr = list(s)
    print(arr)
    for i in range(len(s)):
        new_arr = arr[i:] + arr[:i]   # 왼쪽으로 i만큼 회전
        if is_right_str(new_arr):
            answer += 1
    return answer

def is_right_str(a):
    left_stack = []
    right_stack = []
    
    for e in a:
        if e in left:
            left_stack.append(e)
        else:
            right_stack.append(e)
        
        if left_stack and e == '}' and left_stack[-1] == '{':
            left_stack.pop()
            right_stack.pop()
        elif left_stack and e == ']' and left_stack[-1] == '[':
            left_stack.pop()
            right_stack.pop()
        elif left_stack and e == ')' and left_stack[-1] == '(':
            left_stack.pop()
            right_stack.pop()
            
    if not left_stack and not right_stack:
        return True
    
    return False