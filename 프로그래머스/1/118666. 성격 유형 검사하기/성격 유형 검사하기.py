def solution(survey, choices):
    dict = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    point = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    MBTI = []
    for i, choice in enumerate(choices):
        if choice > 4:
            dict[survey[i][1]] += point[choice]
        elif choice < 4:
            dict[survey[i][0]] += point[choice]
        else: continue
    MBTI.append('R' if dict['R'] >= dict['T'] else 'T')
    MBTI.append('C' if dict['C'] >= dict['F'] else 'F')
    MBTI.append('J' if dict['J'] >= dict['M'] else 'M')
    MBTI.append('A' if dict['A'] >= dict['N'] else 'N')
    
    answer = ''.join(MBTI)
    return answer