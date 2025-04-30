# 테이블은 2차원 행렬로 표현할 수 있으며 열은 컬럼을 나타내고, 행은 튜플
# 첫 번째 컬럼은 기본키로서 모든 튜플에 대해 그 값이 중복되지 않도록 보장
# 튜플을 col번째 컬럼의 값을 기준으로 오름차순 정렬, 만약 그 값이 동일하면 기본키인 첫 번째 컬럼의 값을 기준으로 내림차순 정렬
# S_i를 i 번째 행의 튜플에 대해 각 컬럼의 값을 i 로 나눈 나머지들의 합으로 정의
# row_begin ≤ i ≤ row_end 인 모든 S_i를 누적하여 bitwise XOR 한 값을 해시 값으로서 반환

def solution(data, col, row_begin, row_end):
    # 튜플을 col번째 컬럼의 값을 기준으로 오름차순 정렬, 동일한 값인 경우 첫 번째 컬럼의 값을 기준으로 내림차순 정렬
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    
    # S_i를 i 번째 행의 튜플에 대해 각 컬럼의 값을 i 로 나눈 나머지들의 합으로 정의
    sum_list = []
    for i in range(len(data)):
        tmp_sum = 0
        for j in range(len(data[0])):
            tmp_sum += (data[i][j] % (i + 1))
        sum_list.append(tmp_sum)
    
    # # row_begin ≤ i ≤ row_end 인 모든 S_i를 누적하여 bitwise XOR 한 값을 해시 값으로서 반환
    answer = sum_list[row_begin - 1]
    for i in range(row_begin, row_end):
        answer ^= sum_list[i]
    
    return answer