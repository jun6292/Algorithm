# 도시 이름은 대소문자 구분을 하지 않는 영문자
# LRU, cache hit 1 소요, miss 5 소요
# 입력된 도시이름 배열을 순서대로 처리할 때, "총 실행시간"을 출력
# dictionary에 도시이름을 key로, 캐시에서 안쓰이는 시간을 value로 넣어준다.
# 도시이름을 차례대로 확인한다, 이 때 캐시에 있는 모든 value에 1을 증가한다.
# 도시이름이 캐시에 있다면, cache hit이므로 실행시간 1을 추가하고 value를 0으로 초기화한다.
# 도시이름이 캐시에 없다면, cache miss이므로 실행시간 5를 더하고 캐시가 꽉 찼는지 확인한다.
# 캐시에 여분이 있다면 넣어주고, 꽉 찼다면 value가 가장 큰 것을 교체한다.
def solution(cacheSize, cities):
    answer = 0
    cache_dict = {}
    
    if cacheSize == 0:
        return 5 * len(cities)
        
    for c in cities:
        c_lower = c.lower()
        
        for city in cache_dict:
            cache_dict[city] += 1
        
        if c_lower in cache_dict:
            cache_dict[c_lower] = 0
            answer += 1
        else:
            answer += 5
            if len(cache_dict) >= cacheSize:
                remove_city = find_max_time_in_cache(cache_dict)
                if remove_city != "":
                    del cache_dict[remove_city]
            cache_dict[c_lower] = 0
            
    return answer

def find_max_time_in_cache(dic):
    max_key, max_value = "", 0
    for key, value in dic.items():
        if value > max_value:
            max_key, max_value = key, value

    return max_key