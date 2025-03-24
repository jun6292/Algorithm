# 일정한 금액 지불 시 10일 동안 회원 자격 부여
# 할인 제품 하루에 하나만 구매 가능
# 원하는 제품 문자열 배열 want, 수량 배열 number, 할인 제품 문자열 배열 discount
# 원하는 제품을 '모두 할인 받을 수 있는 회원등록 날짜'의 총 일수를 return
def solution(want, number, discount):
    answer = 0
    want_dict = {}
    
    for i in range(len(discount) - 9):
        for w, n in zip(want, number):
            want_dict[w] = n
        
        ten_days = discount[i : i+10]
        
        for item in ten_days:
            if item in want_dict.keys():
                want_dict[item] -= 1
            else: 
                break

        check = 0
        for w in want_dict.values():
            if w <= 0:
                check += 1
            else:
                break
        
        if check == len(want_dict):
            answer += 1
        
    return answer