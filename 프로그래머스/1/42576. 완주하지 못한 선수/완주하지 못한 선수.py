def solution(participant, completion):
    answer = ''
    dict_part = {}
    
    for i in participant:
        if i in dict_part: dict_part[i]+=1
        else: dict_part[i]=1
    for j in completion:
        if j in dict_part:
            dict_part[j]-=1
    answer = [i for i in dict_part if dict_part[i]==1][0]      
        
    return answer