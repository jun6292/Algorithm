# distance가 10억
def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    left, right = 1, distance
    while left <= right:
        mid = (left + right) // 2
        prev_rock = 0
        delete_rock = 0
        for rock in rocks:
            dist = rock - prev_rock
            if dist < mid:
                delete_rock += 1
                if delete_rock > n:
                    break
            else:
                prev_rock = rock
                
        if delete_rock > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
                
    return answer