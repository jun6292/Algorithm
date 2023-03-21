# repaint를 section의 처음부터 시작해서 롤러 길이 m만큼 더하고 section의 마지막 원소에 도달할 때까지 반복하면 최소 횟수를 구할 수 있다.
def solution(n, m, section):
    answer = 0
    repaint = section[0]
    for i in section:
        if repaint <= i:
            repaint = i + m
            answer += 1
    return answer