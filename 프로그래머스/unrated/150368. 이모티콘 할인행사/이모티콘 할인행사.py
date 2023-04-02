from itertools import product

def solution(users, emoticons):
    answer = []
    discount = [10, 20, 30, 40]
    discount_rate = list(product(discount, repeat = len(emoticons)))    # 모든 가능한 이모티콘 할인율: 4^(len(emoticions))
    for dr in discount_rate:
        sales, subscriber = 0, 0
        for user in users:
            emo_sum = 0 # 모든 이모티콘의 합
            for d, e in zip(dr, emoticons):
                if user[0] <= d:
                    emo_sum += e - (e * d * 0.01) # 할인율이 적용된 이모티콘의 가격
            if emo_sum >= user[1]:  # 이모티콘 구매 비용이 넘어가면
                subscriber += 1 # 이모티콘 플러스 서비스에 가입
            else:
                sales += emo_sum
        answer.append([subscriber, sales])  # 일단 모든 경우의 수 다 넣어놓고
    answer = max(i for i in answer) # 정렬
    return answer