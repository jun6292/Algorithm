def count_divisor(num, limit, power):   # count divisor from 1 to num
    cnt = 0
    # for (int i = 1; i * i <= n; i++) --> for algorithm efficiency
    for i in range(1, int(num ** (1/2)) + 1):
        if num % i == 0:
            if i == num // i:   # i가 num의 제곱근이면 +1
                cnt += 1
            else:
                cnt += 2    # 나머지는 +2
        if cnt > limit: # 약수의 개수가 limit 보다 크면 power return
            return power
    return cnt

def solution(number, limit, power):
    answer = 1
    for i in range(2, number + 1):
        answer += count_divisor(i, limit, power)
    return answer
