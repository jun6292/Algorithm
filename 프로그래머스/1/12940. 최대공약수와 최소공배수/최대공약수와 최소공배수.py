def solution(n, m):
    answer = []
    answer.append(gcd(n, m))
    answer.append((n * m) // gcd(n, m))
    return answer

def gcd(a, b):
    while (b != 0):
        a, b = b, a % b
    return a