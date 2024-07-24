def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))    # n번째 글자 기준으로 오름차순 정렬 후 전체 문자로 정렬