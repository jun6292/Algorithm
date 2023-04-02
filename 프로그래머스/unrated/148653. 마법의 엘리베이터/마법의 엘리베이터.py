# 결론적으로 주어진 정수에서 일의자리만 따지면 됨
def solution(storey):
    answer = 0
    while storey > 0:  # storey의 자릿수를 줄여가며 카운트
        div, mod = divmod(storey, 10)
        if mod > 5: # 엘베 +1
            answer += 10 - mod
        else:   # 엘베 -1
            answer += mod
        if mod > 5 or (mod == 5 and div % 10 >= 5): # *55 같은 case는 *60으로 가는게 돌 1개 절약
            storey = div + 1
        else:
            storey = div
    return answer