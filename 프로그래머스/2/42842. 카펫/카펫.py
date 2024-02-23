def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for row in range(1, total + 1):
        if total % row == 0:
            col = total // row
            if col >= row:
                if (col - 2) * (row - 2) == yellow:
                    answer = [col, row]
    return answer