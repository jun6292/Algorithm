def solution(today, terms, privacies):
    answer = []
    term_and_valid_time = {}    
    t_year, t_month, t_day = int(today[0:4]), int(today[5:7]), int(today[8:]) # 오늘 날짜를 나눌거임
    
    # 약관을 key로 유효기간을 value로 dict 형태로 저장할거임
    for i in terms:
        term, valid_time = i.split()
        term_and_valid_time[term] = int(valid_time)
    
    # enumerate 좋네
    for i, privacy in enumerate(privacies):
        date, p_term = privacy.split()
        year, month, day = int(date[0:4]), int(date[5:7]), int(date[8:])
        
        # 12달 넘으면 년도에 더해줄거임
        month += term_and_valid_time[p_term]
        div, mod = divmod(month, 12)
        year += div
        month = mod
        
        # month가 0일 때 처리
        if month == 0:
            month = 12
            year -= 1
            
        # day가 0일 때 처리
        if day == 1:
            month -= 1
            if month == 0:
                month = 12
                year -= 1
            day = 28
        else:
            day -= 1
        
        # 유효기간이 지났으면 오늘 날짜가 더 클거임. 그래서 파기해야함.
        if t_year > year:  
            answer.append(i + 1)
        elif t_year == year and t_month > month:
            answer.append(i + 1)
        elif t_year == year and t_month == month and t_day > day:
            answer.append(i + 1)

    return answer