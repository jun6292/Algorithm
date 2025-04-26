from itertools import permutations

# 소수가 몇 개인지 return
def solution(numbers):
    number_set = set()
    answer = 0
    for i in range(1, len(numbers) + 1):
        for p in list(permutations(numbers, i)):
            p = ''.join(p)
            if p[0] != '0': # 0으로 시작하는 수는 전부 제외
                number_set.add(int(p))
                
    for num in number_set:
        if is_prime(num):
            answer += 1

    return answer

# 소수 판별
def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int((number ** 0.5)) + 1):
        if number % i == 0:
            return False
    return True