# def solution(n, left, right):
#     answer = []
#     arr2d = [[0 for _ in range(n)] for _ in range(n)] # 2차원 배열
#     for i in range(n):
#         for j in range(n):
#             if j <= i:
#                 arr2d[i][j] = i + 1
#             else:
#                 arr2d[i][j] = j + 1
#     arr1d = [e for row in arr2d for e in row]
#     answer = arr1d[left : right+1]
#     return answer

def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)
    return answer
