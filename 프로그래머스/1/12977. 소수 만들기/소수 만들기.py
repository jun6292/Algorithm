import math

def solution(nums):
    answer = 0
    number_len = len(nums)
    for i in range(number_len):
        for j in range(i + 1, number_len):
            for k in range(j + 1, number_len):
                if is_prime(nums[i] + nums[j] + nums[k]):
                    answer += 1
    return answer

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
