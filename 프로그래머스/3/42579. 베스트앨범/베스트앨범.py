def solution(genres, plays):
    answer = []
    genres_dict, play_dict = {}, {}
    
    for i in range(len(genres)):
        if genres[i] not in genres_dict:
            genres_dict[genres[i]] = [[i, plays[i]]]
        else:
            genres_dict[genres[i]] += [[i, plays[i]]]

    # print(genres_dict)
    # {'classic': [[0, 500], [2, 150], [3, 800]], 'pop': [[1, 600], [4, 2500]]}
    # print(list(genres_dict.values()))
    # [[[0, 10000], [2, 150], [3, 800]], [[1, 600], [4, 2500]]]
    
    # 속한 노래가 많이 재생된 장르 순으로 정렬
    sorted_genres_list = sorted(list(genres_dict.values()), key=lambda x: -sum(song[1] for song in x))
    # print(sorted_genres_list)
    # [[[1, 600], [4, 2500]], [[0, 500], [2, 150], [3, 800]]]

    # 장르 내에서 많이 재생된 순으로, 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 순으로 정렬
    for lst in sorted_genres_list:
        lst.sort(key=lambda x: (-x[1], x[0]))
    
    # 장르 별로 가장 많이 재생된 노래를 최대 두 개까지 수록
    for lst in sorted_genres_list:
        if len(lst) < 2:    # 장르 별 노래 수가 1인 경우
            answer.append(lst[0][0])
        else:
            for i in range(2):
                answer.append(lst[i][0])

    return answer