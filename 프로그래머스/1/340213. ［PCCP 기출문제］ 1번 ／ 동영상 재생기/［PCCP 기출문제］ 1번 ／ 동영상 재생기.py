
# prev -> 10초전 이동 (현재 위치가 10초 미만인 경우 영상 처음으로 이동)
# next -> 10초후 이동 (남은 시간이 10초 미만일 경우 영상 마지막으로 이동)
# 영상 마지막은 동영상의 길이
# 오프닝 건너뛰기 (현재 위치가 오프닝 구간인 경우 오프닝이 끝나는 위치로 이동)

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len_num = str_to_num(video_len)
    cur = str_to_num(pos)
    op_start_num = str_to_num(op_start)
    op_end_num = str_to_num(op_end)
    
    for c in commands:
        if c == "next":
            if cur + 10 > video_len_num:
                cur = video_len_num
            elif op_start_num <= cur <= op_end_num:
                cur = op_end_num
                cur += 10
            elif op_start_num <= cur + 10 <= op_end_num:
                cur = op_end_num
            else:
                cur += 10
        else:
            if cur - 10 < 0:
                cur = 0
            elif op_start_num <= cur - 10 <= op_end_num:
                cur = op_end_num
            elif op_start_num <= cur <= op_end_num:
                cur = op_end_num - 10
            else:
                cur -= 10
                
    if 0 <= cur // 60 < 10:
        answer += '0'
    answer += str(cur // 60)
    answer += ':'
    if 0 <= cur % 60 < 10:
        answer += '0'
    answer += str(cur % 60)
    return answer

def str_to_num(src):
    src_lst = src.split(':')
    return int(src_lst[0]) * 60 + int(src_lst[1])