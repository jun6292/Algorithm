# 1부터 6까지 숫자가 적힌 주사위가 네 개
# 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점
# 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)^2 점
# 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점
# 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점
# 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수
def solution(a, b, c, d):
    answer = 0
    if a == b and b == c and c == d:    # 모두 같은 경우
        answer = 1111 * a
    elif a != b and a != c and a != d and b != c and b != d and c != d: # 모두 다른 경우
        answer += min(a, b, c, d)
    elif a == b and b == c and c != d:  # 3개가 같은 경우
        answer = (10 * a + d) ** 2
    elif a == b and b == d and c != d:
        answer = (10 * a + c) ** 2
    elif a == c and c == d and d != b:
        answer = (10 * a + b) ** 2
    elif b == c and c == d and b != a:
        answer = (10 * b + a) ** 2
    elif a == b and b != c and c == d:  # 2개 2개 같은 경우
        answer = (a + c) * abs(a - c)
    elif a == c and b != c and b == d:
        answer = (a + b) * abs(a - b)
    elif a == d and d != c and b == c:
        answer = (a + c) * abs(a - c)
    elif a == b and b != c and b != d and c != d:
        answer = c * d
    elif a == c and a != b and a != d and b != d:
        answer = b * d
    elif a == d and a != b and a != c and b != c:
        answer = b * c
    elif b == c and b != a and b != d and a != d:
        answer = a * d
    elif b == d and b != a and b != c and a != c:
        answer = a * c
    elif c == d and c != a and c != b and a != b:
        answer = a * b
    

    return answer