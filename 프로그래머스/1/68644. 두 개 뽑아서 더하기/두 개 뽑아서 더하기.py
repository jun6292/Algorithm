def solution(numbers):
    answer = []
    num_len = len(numbers)
    for i in range(num_len):
        for j in range(num_len):
            if i != j and (numbers[i] + numbers[j] not in answer):
                answer.append(numbers[i] + numbers[j])
    answer = sorted(answer)
    return answer