def solution(number, k):
    stack = []
    
    for num in number:
        # 맨 앞에 가장 큰 수가 오기 위함
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    for i in range(k):  # 제거할 숫자가 남았을 때 맨 뒤에서부터 제거
        stack.pop()

    return ''.join(stack)