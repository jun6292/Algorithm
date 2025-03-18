# 몸무게 기준 오름차순 정렬 후, 무게가 가벼운 순서로 보트에 태우자.
def solution(people, limit):
    people.sort()
    
    min_boat_cnt = 0
    start, end = 0, len(people) - 1
    
    while end >= start:
        if limit >= people[end] + people[start]:
            min_boat_cnt += 1
            end -= 1
            start += 1
        else:
            min_boat_cnt += 1
            end -= 1
        
    return min_boat_cnt