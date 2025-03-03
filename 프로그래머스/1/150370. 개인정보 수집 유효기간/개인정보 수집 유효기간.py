def solution(today, terms, privacies):
    answer = []
    #terms를 dict로 변환
    term_dict = {}
    for term in terms:
        term_dict[term.split()[0]] = int(term.split()[1])*28
    
    year, month, day = map(int, today.split("."))
    today_days = year*12*28 + month*28 + day
    
    #privacies의 날짜값을 일수로 변환
    for i, privacy in enumerate(privacies):
        date, term_type = privacy.split()
        year, month, day = map(int,date.split("."))
        total_days = year*12*28 + month*28 + day
        if (total_days + term_dict[term_type] <= today_days):
            answer.append(i+1)
        
    return answer