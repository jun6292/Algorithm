def solution(s):
    answer = []
    ch_dict = {}
    for idx, ch in enumerate(s):
        if ch not in ch_dict.keys():
            answer.append(-1)
            ch_dict[ch] = idx
        else:
            answer.append(idx - ch_dict[ch])
            ch_dict[ch] = idx
    return answer